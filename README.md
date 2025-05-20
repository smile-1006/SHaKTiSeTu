# ShaktiSetu Platform

ShaktiSetu is a comprehensive AI-powered ecosystem designed specifically for women-led MSMEs. The platform connects entrepreneurs with verified buyers, provides digital storefronts, facilitates access to government schemes, offers learning resources, and provides mentorship opportunities - all in one integrated platform.

## Project Structure

The project is organized into two main components:

### Backend (Flask)

Located in `/backend/shaktisetu-backend/`:

- `src/main.py`: Entry point for the Flask application
- `src/models/`: Database models for all modules
- `src/routes/`: API endpoints for all modules
- `src/static/`: Static assets

### Frontend (React)

Located in `/frontend/shaktisetu-frontend/`:

- Modern React application with TypeScript
- Tailwind CSS for styling
- Multi-language support (7 languages)
- Responsive design for all devices

## Features

1. **AI-Powered Marketplace**
   - Connect with verified buyers through intelligent matchmaking
   - Integration with GeM and Amazon Saheli
   - Product listing and management

2. **No-Code Digital Storefront**
   - Drag-and-drop storefront builder
   - WhatsApp and Instagram integration
   - Customizable templates

3. **Procurement Dashboard**
   - Tender alerts and filtering
   - Auto-fill forms
   - Eligibility-based opportunity matching

4. **Micro-Learning Hub**
   - Voice-enabled courses in regional languages
   - Bite-sized learning modules
   - Skill development tracking

5. **Fintech & Logistics Integration**
   - Alternate credit scoring
   - Shipping integrations (Shiprocket, India Post)
   - Payment processing

6. **Mentorship & Peer Networks**
   - Connect with industry mentors
   - Live Q&A sessions
   - WhatsApp group integration

7. **Government Scheme Integration**
   - Eligibility checker for schemes
   - Application guidance
   - Document preparation assistance

8. **News & Success Stories**
   - Inspirational entrepreneur stories
   - Industry news and updates
   - Community engagement

## Multi-Language Support

The platform supports 7 languages:
- English
- Hindi
- Tamil
- Bengali
- Telugu
- Marathi
- Gujarati

## Installation & Setup

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend/shaktisetu-backend
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```
   python -m src.main
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend/shaktisetu-frontend
   ```

2. Install dependencies:
   ```
   pnpm install
   ```

3. Run the development server:
   ```
   pnpm run dev
   ```

## Deployment

### Backend Deployment

The Flask backend can be deployed to any server that supports Python applications. Make sure to:
- Set up a production WSGI server (like Gunicorn)
- Configure a proper database connection
- Set appropriate environment variables

### Frontend Deployment

The React frontend can be built for production using:
```
pnpm run build
```

The resulting build files can be served from any static file server or CDN.

## Technologies Used

- **Backend**: Flask, SQLAlchemy, PyJWT
- **Frontend**: React, TypeScript, Tailwind CSS, shadcn/ui
- **Database**: MySQL (configured)
- **Authentication**: JWT-based authentication

## Future Enhancements

- Advanced AI/ML features for better buyer-seller matching
- Mobile application development
- Enhanced analytics dashboard
- Integration with more payment gateways and logistics providers
