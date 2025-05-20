import React from 'react';
import { useLanguage } from '../hooks/useLanguage';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';

const SuccessStoriesPreview: React.FC = () => {
  const { t } = useLanguage();
  
  // Sample success stories
  const stories = [
    {
      id: 1,
      title: 'From Home Kitchen to National Brand',
      entrepreneur: 'Radha Sharma',
      business: 'Spice Delight',
      industry: 'Food & Beverages',
      description: 'Started with homemade spice blends, now supplies to major retail chains across India.',
      image: '/story1.jpg'
    },
    {
      id: 2,
      title: 'Reviving Traditional Textiles',
      entrepreneur: 'Meena Patel',
      business: 'Threads of India',
      industry: 'Textiles & Handicrafts',
      description: 'Transformed a small weaving unit into a thriving export business, employing 50+ women artisans.',
      image: '/story2.jpg'
    },
    {
      id: 3,
      title: 'Tech Innovation in Rural Healthcare',
      entrepreneur: 'Dr. Lakshmi Rao',
      business: 'MediConnect',
      industry: 'Healthcare Technology',
      description: 'Developed a mobile platform connecting rural patients with urban doctors, serving 100+ villages.',
      image: '/story3.jpg'
    }
  ];

  return (
    <section className="py-12 bg-gray-50">
      <div className="container mx-auto px-4">
        <div className="text-center mb-10">
          <h2 className="text-2xl font-bold mb-4">Success Stories</h2>
          <p className="text-gray-600 max-w-2xl mx-auto">
            Get inspired by the journeys of women entrepreneurs who have overcome challenges and built thriving businesses.
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {stories.map(story => (
            <Card key={story.id} className="overflow-hidden">
              <div className="h-48 bg-gray-200 relative">
                {/* In a real implementation, this would be an actual image */}
                <div className="absolute inset-0 flex items-center justify-center text-gray-500">
                  Entrepreneur Photo
                </div>
              </div>
              <CardHeader>
                <CardTitle className="text-lg">{story.title}</CardTitle>
                <div className="text-sm text-gray-500">{story.entrepreneur} | {story.business}</div>
              </CardHeader>
              <CardContent>
                <div className="mb-3">
                  <span className="inline-block px-2 py-1 text-xs bg-primary/10 text-primary rounded-full">
                    {story.industry}
                  </span>
                </div>
                <p className="text-sm text-gray-600 mb-4">{story.description}</p>
                <Button variant="outline" className="w-full">Read Full Story</Button>
              </CardContent>
            </Card>
          ))}
        </div>
        
        <div className="mt-12 text-center">
          <h3 className="text-xl font-semibold mb-4">Share Your Story</h3>
          <p className="text-gray-600 max-w-2xl mx-auto mb-6">
            Inspire other entrepreneurs by sharing your business journey and success with the ShaktiSetu community.
          </p>
          <Button>Submit Your Story</Button>
        </div>
      </div>
    </section>
  );
};

export default SuccessStoriesPreview;
