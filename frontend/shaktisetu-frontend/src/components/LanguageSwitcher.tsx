import React from 'react';
import { Button } from './ui/button';
import { useLanguage } from '../hooks/useLanguage';

// Define the available languages
const languages = [
  { code: 'english', label: 'English' },
  { code: 'hindi', label: 'हिंदी' },
  { code: 'tamil', label: 'தமிழ்' },
  { code: 'bengali', label: 'বাংলা' },
  { code: 'telugu', label: 'తెలుగు' },
  { code: 'marathi', label: 'मराठी' },
  { code: 'gujarati', label: 'ગુજરાતી' },
];

const LanguageSwitcher: React.FC = () => {
  const { language, setLanguage } = useLanguage();

  return (
    <div className="flex flex-wrap gap-2">
      {languages.map((lang) => (
        <Button
          key={lang.code}
          variant={language === lang.code ? "default" : "outline"}
          size="sm"
          onClick={() => setLanguage(lang.code as any)}
          className="text-sm"
        >
          {lang.label}
        </Button>
      ))}
    </div>
  );
};

export default LanguageSwitcher;
