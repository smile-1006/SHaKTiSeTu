import React from 'react';
import { useLanguage } from '../hooks/useLanguage';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';

const MentorshipPreview: React.FC = () => {
  const { t } = useLanguage();
  
  // Sample mentors for the mentorship preview
  const mentors = [
    {
      id: 1,
      name: 'Sunita Reddy',
      expertise: 'Business Strategy',
      experience: '15 years',
      bio: 'Former CEO with expertise in scaling businesses from startup to enterprise level.',
      image: '/mentor1.jpg'
    },
    {
      id: 2,
      name: 'Kavita Desai',
      expertise: 'Marketing & Branding',
      experience: '12 years',
      bio: 'Marketing expert specializing in digital strategies for small businesses.',
      image: '/mentor2.jpg'
    },
    {
      id: 3,
      name: 'Neha Sharma',
      expertise: 'Financial Planning',
      experience: '10 years',
      bio: 'Financial advisor helping women entrepreneurs secure funding and manage growth.',
      image: '/mentor3.jpg'
    }
  ];

  return (
    <section className="py-12 bg-white">
      <div className="container mx-auto px-4">
        <div className="text-center mb-10">
          <h2 className="text-2xl font-bold mb-4">Mentorship & Peer Networks</h2>
          <p className="text-gray-600 max-w-2xl mx-auto">
            Connect with experienced mentors and like-minded entrepreneurs to grow your business.
            Get personalized guidance and join supportive communities.
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {mentors.map(mentor => (
            <Card key={mentor.id} className="overflow-hidden">
              <div className="h-48 bg-gray-200 relative">
                {/* In a real implementation, this would be an actual image */}
                <div className="absolute inset-0 flex items-center justify-center text-gray-500">
                  Mentor Photo
                </div>
              </div>
              <CardHeader>
                <CardTitle className="text-lg">{mentor.name}</CardTitle>
                <div className="text-sm font-medium text-primary">{mentor.expertise}</div>
              </CardHeader>
              <CardContent>
                <div className="mb-3">
                  <div className="text-xs text-gray-500">Experience</div>
                  <div className="text-sm">{mentor.experience}</div>
                </div>
                <p className="text-sm text-gray-600 mb-4">{mentor.bio}</p>
                <Button className="w-full">Book a Session</Button>
              </CardContent>
            </Card>
          ))}
        </div>
        
        <div className="mt-12 grid grid-cols-1 md:grid-cols-2 gap-8">
          <div className="bg-gray-100 p-6 rounded-lg">
            <h3 className="text-xl font-semibold mb-4">Live Q&A Sessions</h3>
            <p className="text-gray-600 mb-4">
              Join interactive sessions with industry experts and get your business questions answered in real-time.
            </p>
            <Button variant="outline">View Upcoming Sessions</Button>
          </div>
          
          <div className="bg-gray-100 p-6 rounded-lg">
            <h3 className="text-xl font-semibold mb-4">WhatsApp Peer Groups</h3>
            <p className="text-gray-600 mb-4">
              Connect with other women entrepreneurs in your industry through moderated WhatsApp groups.
            </p>
            <Button variant="outline">Join a Group</Button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default MentorshipPreview;
