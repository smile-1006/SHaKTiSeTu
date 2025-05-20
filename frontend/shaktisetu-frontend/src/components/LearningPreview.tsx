import React from 'react';
import { useLanguage } from '../hooks/useLanguage';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';

const LearningPreview: React.FC = () => {
  const { t } = useLanguage();
  
  // Sample courses for the learning preview
  const courses = [
    {
      id: 1,
      title: 'Financial Management for Small Businesses',
      instructor: 'Priya Sharma',
      duration: '4 hours',
      level: 'Beginner',
      language: 'Hindi, English',
      image: '/course1.jpg'
    },
    {
      id: 2,
      title: 'Digital Marketing Essentials',
      instructor: 'Meera Patel',
      duration: '6 hours',
      level: 'Intermediate',
      language: 'Tamil, English',
      image: '/course2.jpg'
    },
    {
      id: 3,
      title: 'Supply Chain Management',
      instructor: 'Anjali Gupta',
      duration: '5 hours',
      level: 'Advanced',
      language: 'Bengali, English',
      image: '/course3.jpg'
    }
  ];

  return (
    <section className="py-12 bg-gray-50">
      <div className="container mx-auto px-4">
        <div className="text-center mb-10">
          <h2 className="text-2xl font-bold mb-4">Micro-Learning Hub</h2>
          <p className="text-gray-600 max-w-2xl mx-auto">
            Access voice-enabled courses in regional languages to grow your business skills.
            Learn at your own pace with bite-sized lessons.
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {courses.map(course => (
            <Card key={course.id} className="overflow-hidden">
              <div className="h-48 bg-gray-200 relative">
                {/* In a real implementation, this would be an actual image */}
                <div className="absolute inset-0 flex items-center justify-center text-gray-500">
                  Course Image
                </div>
              </div>
              <CardHeader>
                <CardTitle className="text-lg">{course.title}</CardTitle>
                <div className="text-sm text-gray-500">By {course.instructor}</div>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-2 gap-2 mb-4">
                  <div>
                    <div className="text-xs text-gray-500">Duration</div>
                    <div className="text-sm">{course.duration}</div>
                  </div>
                  <div>
                    <div className="text-xs text-gray-500">Level</div>
                    <div className="text-sm">{course.level}</div>
                  </div>
                  <div className="col-span-2">
                    <div className="text-xs text-gray-500">Languages</div>
                    <div className="text-sm">{course.language}</div>
                  </div>
                </div>
                <Button className="w-full">Start Learning</Button>
              </CardContent>
            </Card>
          ))}
        </div>
        
        <div className="mt-12 text-center">
          <h3 className="text-xl font-semibold mb-4">Voice-Enabled Learning</h3>
          <p className="text-gray-600 max-w-2xl mx-auto mb-6">
            Our courses are available in multiple regional languages with voice narration,
            making learning accessible for everyone regardless of literacy level.
          </p>
          <Button>Browse All Courses</Button>
        </div>
      </div>
    </section>
  );
};

export default LearningPreview;
