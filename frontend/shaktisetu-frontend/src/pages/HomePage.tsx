import React from 'react';
import { useLanguage } from '../hooks/useLanguage';
import Hero from '../components/Hero';
import FeatureCard from '../components/FeatureCard';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

const HomePage: React.FC = () => {
  const { t } = useLanguage();
  
  const features = [
    {
      title: 'AI-Powered Marketplace',
      description: 'Connect with verified buyers through our intelligent matchmaking system. Integrate with GeM and Amazon Saheli.',
      icon: <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="8" cy="21" r="1"/><circle cx="19" cy="21" r="1"/><path d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12"/></svg>,
      buttonText: 'Explore Marketplace',
      buttonLink: '/marketplace'
    },
    {
      title: 'No-Code Digital Storefront',
      description: 'Create your own digital storefront with our drag-and-drop builder. Integrate with WhatsApp and Instagram.',
      icon: <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M3 9h18v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V9Z"/><path d="m3 9 2.45-4.9A2 2 0 0 1 7.24 3h9.52a2 2 0 0 1 1.8 1.1L21 9"/><path d="M12 3v6"/></svg>,
      buttonText: 'Create Storefront',
      buttonLink: '/storefront'
    },
    {
      title: 'Procurement Dashboard',
      description: 'Get alerts for relevant tenders, auto-fill forms, and filter opportunities based on eligibility.',
      icon: <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M7 7h10"/><path d="M7 12h10"/><path d="M7 17h10"/></svg>,
      buttonText: 'View Tenders',
      buttonLink: '/procurement'
    },
    {
      title: 'Micro-Learning Hub',
      description: 'Access voice-enabled courses in regional languages to grow your business skills.',
      icon: <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg>,
      buttonText: 'Start Learning',
      buttonLink: '/learning'
    },
    {
      title: 'Fintech & Logistics',
      description: 'Access alternate credit scoring and shipping integrations with Shiprocket and India Post.',
      icon: <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect width="20" height="14" x="2" y="5" rx="2"/><line x1="2" x2="22" y1="10" y2="10"/></svg>,
      buttonText: 'Financial Tools',
      buttonLink: '/fintech'
    },
    {
      title: 'Mentorship & Peer Networks',
      description: 'Connect with mentors for live Q&A sessions and join WhatsApp groups with like-minded entrepreneurs.',
      icon: <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M14 19a6 6 0 0 0-12 0"/><circle cx="8" cy="9" r="4"/><path d="M22 19a6 6 0 0 0-6-6 4 4 0 1 0 0-8"/></svg>,
      buttonText: 'Find Mentors',
      buttonLink: '/mentorship'
    },
    {
      title: 'Government Scheme Integration',
      description: 'Check eligibility for various government schemes and get guidance on application process.',
      icon: <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M2 20h.01"/><path d="M7 20v-4"/><path d="M12 20v-8"/><path d="M17 20V8"/><path d="M22 4v16"/></svg>,
      buttonText: 'Explore Schemes',
      buttonLink: '/schemes'
    },
    {
      title: 'Success Stories',
      description: 'Get inspired by stories of women entrepreneurs who have grown their businesses through ShaktiSetu.',
      icon: <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 20.94c1.5 0 2.75 1.06 4 1.06 3 0 6-8 6-12.22A4.91 4.91 0 0 0 17 5c-2.22 0-4 1.44-5 2-1-.56-2.78-2-5-2a4.9 4.9 0 0 0-5 4.78C2 14 5 22 8 22c1.25 0 2.5-1.06 4-1.06Z"/><path d="M10 2c1 .5 2 2 2 5"/></svg>,
      buttonText: 'Read Stories',
      buttonLink: '/news'
    }
  ];

  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      
      <main className="flex-grow">
        <Hero />
        
        <section className="py-16 bg-gray-50">
          <div className="container mx-auto px-4">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-bold mb-4">Our Platform Features</h2>
              <p className="text-gray-600 max-w-2xl mx-auto">
                ShaktiSetu provides a comprehensive ecosystem for women entrepreneurs to grow their businesses,
                access new markets, and build valuable skills.
              </p>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              {features.map((feature, index) => (
                <FeatureCard
                  key={index}
                  title={feature.title}
                  description={feature.description}
                  icon={feature.icon}
                  buttonText={feature.buttonText}
                  buttonLink={feature.buttonLink}
                />
              ))}
            </div>
          </div>
        </section>
        
        <section className="py-16 bg-white">
          <div className="container mx-auto px-4">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-bold mb-4">How It Works</h2>
              <p className="text-gray-600 max-w-2xl mx-auto">
                Getting started with ShaktiSetu is simple. Follow these steps to begin your journey.
              </p>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              <div className="text-center">
                <div className="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-4">
                  <span className="text-primary text-2xl font-bold">1</span>
                </div>
                <h3 className="text-xl font-semibold mb-2">Register Your Business</h3>
                <p className="text-gray-600">
                  Create your account, verify your business details, and set up your profile.
                </p>
              </div>
              
              <div className="text-center">
                <div className="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-4">
                  <span className="text-primary text-2xl font-bold">2</span>
                </div>
                <h3 className="text-xl font-semibold mb-2">Create Your Storefront</h3>
                <p className="text-gray-600">
                  Use our no-code builder to create your digital storefront and showcase your products.
                </p>
              </div>
              
              <div className="text-center">
                <div className="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-4">
                  <span className="text-primary text-2xl font-bold">3</span>
                </div>
                <h3 className="text-xl font-semibold mb-2">Connect & Grow</h3>
                <p className="text-gray-600">
                  Get matched with buyers, access learning resources, and scale your business.
                </p>
              </div>
            </div>
          </div>
        </section>
        
        <section className="py-16 bg-primary text-white">
          <div className="container mx-auto px-4 text-center">
            <h2 className="text-3xl font-bold mb-6">Ready to Grow Your Business?</h2>
            <p className="text-xl mb-8 max-w-2xl mx-auto">
              Join thousands of women entrepreneurs who are scaling their businesses with ShaktiSetu.
            </p>
            <Button size="lg" className="bg-white text-primary hover:bg-gray-100">
              Register Now
            </Button>
          </div>
        </section>
      </main>
      
      <Footer />
    </div>
  );
};

export default HomePage;
