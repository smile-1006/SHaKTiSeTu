import React from 'react';
import { useLanguage } from '../hooks/useLanguage';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';

const MarketplacePreview: React.FC = () => {
  const { t } = useLanguage();
  
  // Sample products for the marketplace preview
  const products = [
    {
      id: 1,
      name: 'Handcrafted Textile Products',
      seller: 'Lakshmi Textiles',
      price: '₹1,200',
      image: '/product1.jpg',
      category: 'Textiles'
    },
    {
      id: 2,
      name: 'Organic Spice Collection',
      seller: 'Anita Spices',
      price: '₹850',
      image: '/product2.jpg',
      category: 'Food & Beverages'
    },
    {
      id: 3,
      name: 'Handmade Jewelry Set',
      seller: 'Priya Crafts',
      price: '₹1,500',
      image: '/product3.jpg',
      category: 'Jewelry'
    },
    {
      id: 4,
      name: 'Natural Skincare Kit',
      seller: 'Herbal Beauty',
      price: '₹950',
      image: '/product4.jpg',
      category: 'Beauty & Wellness'
    }
  ];

  return (
    <section className="py-12 bg-gray-50">
      <div className="container mx-auto px-4">
        <div className="flex justify-between items-center mb-8">
          <h2 className="text-2xl font-bold">Featured Products</h2>
          <Button variant="outline">View All Products</Button>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {products.map(product => (
            <Card key={product.id} className="overflow-hidden">
              <div className="h-48 bg-gray-200 relative">
                {/* In a real implementation, this would be an actual image */}
                <div className="absolute inset-0 flex items-center justify-center text-gray-500">
                  Product Image
                </div>
              </div>
              <CardHeader>
                <CardTitle className="text-lg">{product.name}</CardTitle>
                <div className="text-sm text-gray-500">{product.seller}</div>
              </CardHeader>
              <CardContent>
                <div className="flex justify-between items-center">
                  <div className="font-bold">{product.price}</div>
                  <div className="text-xs px-2 py-1 bg-primary/10 text-primary rounded-full">
                    {product.category}
                  </div>
                </div>
                <Button className="w-full mt-4">View Details</Button>
              </CardContent>
            </Card>
          ))}
        </div>
        
        <div className="mt-12 text-center">
          <h3 className="text-xl font-semibold mb-4">AI-Powered Matchmaking</h3>
          <p className="text-gray-600 max-w-2xl mx-auto mb-6">
            Our intelligent system connects you with verified buyers based on your products and business profile.
          </p>
          <Button>Find Buyers for Your Products</Button>
        </div>
      </div>
    </section>
  );
};

export default MarketplacePreview;
