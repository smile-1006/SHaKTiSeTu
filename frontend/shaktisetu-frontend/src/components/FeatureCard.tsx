import React from 'react';
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';

interface FeatureCardProps {
  title: string;
  description: string;
  icon: React.ReactNode;
  buttonText: string;
  buttonLink: string;
}

const FeatureCard: React.FC<FeatureCardProps> = ({ 
  title, 
  description, 
  icon, 
  buttonText, 
  buttonLink 
}) => {
  return (
    <Card className="h-full flex flex-col">
      <CardHeader>
        <div className="w-12 h-12 flex items-center justify-center rounded-full bg-primary/10 text-primary mb-4">
          {icon}
        </div>
        <CardTitle>{title}</CardTitle>
        <CardDescription>{description}</CardDescription>
      </CardHeader>
      <CardContent className="flex-grow">
        {/* Additional content can go here */}
      </CardContent>
      <CardFooter>
        <Button asChild className="w-full">
          <a href={buttonLink}>{buttonText}</a>
        </Button>
      </CardFooter>
    </Card>
  );
};

export default FeatureCard;
