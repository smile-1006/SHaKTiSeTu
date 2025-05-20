import React from 'react';
import { useLanguage } from '../hooks/useLanguage';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';

const ProcurementPreview: React.FC = () => {
  const { t } = useLanguage();
  
  // Sample tenders for the procurement preview
  const tenders = [
    {
      id: 1,
      title: 'Supply of Handcrafted Textile Products',
      organization: 'Ministry of Textiles',
      value: '₹25 Lakhs',
      deadline: '15 June 2025',
      category: 'Textiles',
      image: '/tender1.jpg'
    },
    {
      id: 2,
      title: 'Organic Food Products for Government Canteens',
      organization: 'Food Corporation of India',
      value: '₹18 Lakhs',
      deadline: '22 June 2025',
      category: 'Food & Beverages',
      image: '/tender2.jpg'
    },
    {
      id: 3,
      title: 'Handicraft Items for Government Exhibitions',
      organization: 'Ministry of Culture',
      value: '₹12 Lakhs',
      deadline: '30 June 2025',
      category: 'Handicrafts',
      image: '/tender3.jpg'
    }
  ];

  return (
    <section className="py-12 bg-white">
      <div className="container mx-auto px-4">
        <div className="text-center mb-10">
          <h2 className="text-2xl font-bold mb-4">Procurement Dashboard</h2>
          <p className="text-gray-600 max-w-2xl mx-auto">
            Get alerts for relevant tenders, auto-fill forms, and filter opportunities based on eligibility.
            Access government and private procurement opportunities tailored to your business.
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {tenders.map(tender => (
            <Card key={tender.id} className="overflow-hidden">
              <div className="h-12 bg-primary/10 flex items-center justify-center">
                <span className="text-primary font-medium">{tender.category}</span>
              </div>
              <CardHeader>
                <CardTitle className="text-lg">{tender.title}</CardTitle>
                <div className="text-sm text-gray-500">{tender.organization}</div>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-2 gap-2 mb-4">
                  <div>
                    <div className="text-xs text-gray-500">Value</div>
                    <div className="text-sm font-medium">{tender.value}</div>
                  </div>
                  <div>
                    <div className="text-xs text-gray-500">Deadline</div>
                    <div className="text-sm font-medium">{tender.deadline}</div>
                  </div>
                </div>
                <div className="flex gap-2">
                  <Button variant="outline" className="flex-1">View Details</Button>
                  <Button className="flex-1">Apply Now</Button>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
        
        <div className="mt-12 grid grid-cols-1 md:grid-cols-2 gap-8">
          <div className="bg-gray-100 p-6 rounded-lg">
            <h3 className="text-xl font-semibold mb-4">Auto-Fill Forms</h3>
            <p className="text-gray-600 mb-4">
              Save time with our intelligent form filling system that automatically populates tender applications with your business information.
            </p>
            <Button variant="outline">Learn More</Button>
          </div>
          
          <div className="bg-gray-100 p-6 rounded-lg">
            <h3 className="text-xl font-semibold mb-4">Eligibility Filters</h3>
            <p className="text-gray-600 mb-4">
              Only see opportunities that match your business profile and eligibility criteria, saving you time and effort.
            </p>
            <Button variant="outline">Set Up Filters</Button>
          </div>
        </div>
        
        <div className="mt-12 text-center">
          <h3 className="text-xl font-semibold mb-4">GeM Integration</h3>
          <p className="text-gray-600 max-w-2xl mx-auto mb-6">
            Seamlessly connect with the Government e-Marketplace (GeM) to access a wide range of procurement opportunities.
          </p>
          <Button>Connect with GeM</Button>
        </div>
      </div>
    </section>
  );
};

export default ProcurementPreview;
