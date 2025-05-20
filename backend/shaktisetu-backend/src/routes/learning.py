from flask import Blueprint, jsonify, request
from src.models.learning import Course, CourseModule, CourseLesson, UserCourseProgress
from src.models.user import db

learning_bp = Blueprint('learning', __name__)

# Course endpoints
@learning_bp.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([course.to_dict() for course in courses])

@learning_bp.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    return jsonify(course.to_dict())

@learning_bp.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    
    if not data or not all(k in data for k in ('title', 'description', 'category', 'level', 'language')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    course = Course(
        title=data['title'],
        description=data['description'],
        category=data['category'],
        level=data['level'],
        language=data['language'],
        duration_minutes=data.get('duration_minutes'),
        thumbnail_url=data.get('thumbnail_url'),
        is_published=data.get('is_published', False)
    )
    
    db.session.add(course)
    db.session.commit()
    
    return jsonify(course.to_dict()), 201

@learning_bp.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    course = Course.query.get_or_404(course_id)
    data = request.get_json()
    
    for key, value in data.items():
        if hasattr(course, key):
            setattr(course, key, value)
    
    db.session.commit()
    return jsonify(course.to_dict())

@learning_bp.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return jsonify({'message': 'Course deleted successfully'})

# Course Module endpoints
@learning_bp.route('/courses/<int:course_id>/modules', methods=['GET'])
def get_modules(course_id):
    modules = CourseModule.query.filter_by(course_id=course_id).order_by(CourseModule.position).all()
    return jsonify([module.to_dict() for module in modules])

@learning_bp.route('/modules/<int:module_id>', methods=['GET'])
def get_module(module_id):
    module = CourseModule.query.get_or_404(module_id)
    return jsonify(module.to_dict())

@learning_bp.route('/courses/<int:course_id>/modules', methods=['POST'])
def create_module(course_id):
    data = request.get_json()
    
    if not data or not all(k in data for k in ('title',)):
        return jsonify({'error': 'Missing required fields'}), 400
    
    module = CourseModule(
        course_id=course_id,
        title=data['title'],
        description=data.get('description'),
        position=data.get('position', 0)
    )
    
    db.session.add(module)
    db.session.commit()
    
    return jsonify(module.to_dict()), 201

# Course Lesson endpoints
@learning_bp.route('/modules/<int:module_id>/lessons', methods=['GET'])
def get_lessons(module_id):
    lessons = CourseLesson.query.filter_by(module_id=module_id).order_by(CourseLesson.position).all()
    return jsonify([lesson.to_dict() for lesson in lessons])

@learning_bp.route('/lessons/<int:lesson_id>', methods=['GET'])
def get_lesson(lesson_id):
    lesson = CourseLesson.query.get_or_404(lesson_id)
    return jsonify(lesson.to_dict())

@learning_bp.route('/modules/<int:module_id>/lessons', methods=['POST'])
def create_lesson(module_id):
    data = request.get_json()
    
    if not data or not all(k in data for k in ('title', 'content_type')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    lesson = CourseLesson(
        module_id=module_id,
        title=data['title'],
        content_type=data['content_type'],
        content_url=data.get('content_url'),
        content_text=data.get('content_text'),
        duration_minutes=data.get('duration_minutes'),
        position=data.get('position', 0)
    )
    
    db.session.add(lesson)
    db.session.commit()
    
    return jsonify(lesson.to_dict()), 201

# User Progress endpoints
@learning_bp.route('/users/<int:user_id>/progress', methods=['GET'])
def get_user_progress(user_id):
    progress = UserCourseProgress.query.filter_by(user_id=user_id).all()
    return jsonify([p.to_dict() for p in progress])

@learning_bp.route('/users/<int:user_id>/progress/<int:lesson_id>', methods=['POST', 'PUT'])
def update_user_progress(user_id, lesson_id):
    data = request.get_json()
    
    progress = UserCourseProgress.query.filter_by(user_id=user_id, lesson_id=lesson_id).first()
    
    if not progress:
        progress = UserCourseProgress(
            user_id=user_id,
            lesson_id=lesson_id,
            completed=data.get('completed', False),
            progress_percentage=data.get('progress_percentage', 0),
            last_position=data.get('last_position', 0)
        )
        db.session.add(progress)
    else:
        if 'completed' in data:
            progress.completed = data['completed']
        if 'progress_percentage' in data:
            progress.progress_percentage = data['progress_percentage']
        if 'last_position' in data:
            progress.last_position = data['last_position']
    
    db.session.commit()
    return jsonify(progress.to_dict())
