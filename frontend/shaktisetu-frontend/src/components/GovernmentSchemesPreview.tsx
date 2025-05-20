import React from 'react';
import { useLanguage } from '../hooks/useLanguage';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';

const GovernmentSchemesPreview: React.FC = () => {
  const { t } = useLanguage();
  
  // Sample government schemes
  const schemes = [
    {
      id: 1,
      name: 'Pradhan Mantri Mudra Yojana',
      ministry: 'Ministry of Finance',
      description: 'Loans up to ₹10 lakh for small businesses without collateral',
      eligibility: 'Small businesses, entrepreneurs, MSMEs',
      image: '/scheme1.jpg'
    },
    {
      id: 2,
      name: 'Stand-Up India',
      ministry: 'Ministry of Finance',
      description: 'Loans between ₹10 lakh and ₹1 crore for SC/ST and women entrepreneurs',
      eligibility: 'SC/ST and women entrepreneurs',
      image: '/scheme2.jpg'
    },
    {
      id: 3,
      name: 'Prime Minister's Employment Generation Programme',
      ministry: 'Ministry of MSME',
      description: 'Credit-linked subsidy for setting up micro-enterprises',
      eligibility: 'Individuals above 18 years, self-help groups',
      image: '/scheme3.jpg'
    }
  ];

  return (
    <section className="py-12 bg-gray-50">
      <div className="container mx-auto px-4">
        <div className="text-center mb-10">
          <h2 className="text-2xl font-bold mb-4">Government Scheme Integration</h2>
          <p className="text-gray-600 max-w-2xl mx-auto">
            Check your eligibility for various government schemes and get guidance on the application process.
            Access funding, subsidies, and support programs designed for women entrepreneurs.
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {schemes.map(scheme => (
            <Card key={scheme.id} className="overflow-hidden">
              <div className="h-32 bg-gray-200 relative">
                {/* In a real implementation, this would be an actual image */}
                <div className="absolute inset-0 flex items-center justify-center text-gray-500">
                  Scheme Logo
                </div>
              </div>
              <CardHeader>
                <CardTitle className="text-lg">{scheme.name}</CardTitle>
                <div className="text-sm text-gray-500">{scheme.ministry}</div>
              </CardHeader>
              <CardContent>
                <p className="text-sm text-gray-600 mb-3">{scheme.description}</p>
                <div className="mb-4">
                  <div className="text-xs text-gray-500">Eligibility</div>
                  <div className="text-sm">{scheme.eligibility}</div>
                </div>
                <div className="flex gap-2">
                  <Button variant="outline" className="flex-1">Check Eligibility</Button>
                  <Button className="flex-1">Apply Now</Button>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
        
        <div className="mt-12 bg-white p-6 rounded-lg shadow-sm">
          <h3 className="text-xl font-semibold mb-4">Eligibility Checker</h3>
          <p className="text-gray-600 mb-6">
            Our AI-powered eligibility checker helps you find government schemes that match your business profile.
            Get personalized recommendations and application guidance.
          </p>
          <div className="flex justify-center">
            <Button size="lg">Find Schemes for Your Business</Button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default GovernmentSchemesPreview;
