import React from 'react';
import { useLanguage } from '../hooks/useLanguage';
import { Button } from './ui/button';

const Hero: React.FC = () => {
  const { t } = useLanguage();
  
  return (
    <div className="bg-gradient-to-r from-purple-600 to-indigo-600 text-white">
      <div className="container mx-auto px-4 py-16 md:py-24">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
          <div>
            <h1 className="text-4xl md:text-5xl font-bold mb-4">
              {t('app.title')}
            </h1>
            <p className="text-xl mb-6">
              An AI-powered ecosystem designed specifically for women-led MSMEs
            </p>
            <p className="mb-8">
              Connect with verified buyers, create digital storefronts, access government schemes, 
              learn new skills, and get mentorship - all in one platform.
            </p>
            <div className="flex flex-wrap gap-4">
              <Button size="lg" className="bg-white text-purple-600 hover:bg-gray-100">
                Join Marketplace
              </Button>
              <Button size="lg" variant="outline" className="border-white text-white hover:bg-white hover:text-purple-600">
                Create Storefront
              </Button>
            </div>
          </div>
          <div className="flex justify-center">
            <div className="bg-white p-4 rounded-lg shadow-lg">
              <img 
                src="/hero-image.svg" 
                alt="ShaktiSetu Platform" 
                className="max-w-full h-auto"
                style={{ maxHeight: '400px' }}
              />
            </div>
          </div>
        </div>
        
        <div className="mt-16 grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
          <div>
            <div className="text-4xl font-bold">1000+</div>
            <div className="text-gray-200">Women Entrepreneurs</div>
          </div>
          <div>
            <div className="text-4xl font-bold">500+</div>
            <div className="text-gray-200">Verified Buyers</div>
          </div>
          <div>
            <div className="text-4xl font-bold">₹10Cr+</div>
            <div className="text-gray-200">Business Generated</div>
          </div>
          <div>
            <div className="text-4xl font-bold">50+</div>
            <div className="text-gray-200">Government Schemes</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Hero;
