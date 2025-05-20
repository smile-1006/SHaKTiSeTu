import { createContext, useContext, useState, ReactNode, useEffect } from 'react';

// Define available languages
export type Language = 'english' | 'hindi' | 'tamil' | 'bengali' | 'telugu' | 'marathi' | 'gujarati';

interface LanguageContextType {
  language: Language;
  setLanguage: (language: Language) => void;
  t: (key: string) => string;
}

// Create context
const LanguageContext = createContext<LanguageContextType | undefined>(undefined);

// Translation data - this would be expanded with actual translations
const translations: Record<Language, Record<string, string>> = {
  english: {
    'app.title': 'ShaktiSetu',
    'app.tagline': 'Empowering Women-led MSMEs',
    'nav.home': 'Home',
    'nav.marketplace': 'Marketplace',
    'nav.storefront': 'Storefront',
    'nav.procurement': 'Procurement',
    'nav.learning': 'Learning',
    'nav.mentorship': 'Mentorship',
    'nav.schemes': 'Government Schemes',
    'nav.login': 'Login',
    'nav.register': 'Register',
    'auth.email': 'Email',
    'auth.password': 'Password',
    'auth.login': 'Login',
    'auth.register': 'Register',
    'auth.fullName': 'Full Name',
    'auth.businessName': 'Business Name',
    'auth.phone': 'Phone Number',
    // Add more translations as needed
  },
  hindi: {
    'app.title': 'शक्तिसेतु',
    'app.tagline': 'महिला नेतृत्व वाले MSMEs को सशक्त बनाना',
    'nav.home': 'होम',
    'nav.marketplace': 'मार्केटप्लेस',
    'nav.storefront': 'स्टोरफ्रंट',
    'nav.procurement': 'प्रोक्योरमेंट',
    'nav.learning': 'लर्निंग',
    'nav.mentorship': 'मेंटरशिप',
    'nav.schemes': 'सरकारी योजनाएं',
    'nav.login': 'लॉगिन',
    'nav.register': 'रजिस्टर',
    'auth.email': 'ईमेल',
    'auth.password': 'पासवर्ड',
    'auth.login': 'लॉगिन',
    'auth.register': 'रजिस्टर',
    'auth.fullName': 'पूरा नाम',
    'auth.businessName': 'व्यापार का नाम',
    'auth.phone': 'फोन नंबर',
    // Add more translations as needed
  },
  tamil: {
    'app.title': 'சக்திசேது',
    'app.tagline': 'பெண்கள் தலைமையிலான MSMEs-ஐ அதிகாரப்படுத்துதல்',
    'nav.home': 'முகப்பு',
    'nav.marketplace': 'சந்தை',
    'nav.storefront': 'கடை முகப்பு',
    'nav.procurement': 'கொள்முதல்',
    'nav.learning': 'கற்றல்',
    'nav.mentorship': 'வழிகாட்டல்',
    'nav.schemes': 'அரசு திட்டங்கள்',
    'nav.login': 'உள்நுழைய',
    'nav.register': 'பதிவு செய்ய',
    'auth.email': 'மின்னஞ்சல்',
    'auth.password': 'கடவுச்சொல்',
    'auth.login': 'உள்நுழைய',
    'auth.register': 'பதிவு செய்ய',
    'auth.fullName': 'முழு பெயர்',
    'auth.businessName': 'வணிக பெயர்',
    'auth.phone': 'தொலைபேசி எண்',
    // Add more translations as needed
  },
  bengali: {
    'app.title': 'শক্তিসেতু',
    'app.tagline': 'মহিলা নেতৃত্বাধীন MSMEs-কে ক্ষমতায়ন',
    'nav.home': 'হোম',
    'nav.marketplace': 'মার্কেটপ্লেস',
    'nav.storefront': 'স্টোরফ্রন্ট',
    'nav.procurement': 'প্রকিউরমেন্ট',
    'nav.learning': 'লার্নিং',
    'nav.mentorship': 'মেন্টরশিপ',
    'nav.schemes': 'সরকারি প্রকল্প',
    'nav.login': 'লগইন',
    'nav.register': 'রেজিস্টার',
    'auth.email': 'ইমেইল',
    'auth.password': 'পাসওয়ার্ড',
    'auth.login': 'লগইন',
    'auth.register': 'রেজিস্টার',
    'auth.fullName': 'পুরো নাম',
    'auth.businessName': 'ব্যবসার নাম',
    'auth.phone': 'ফোন নম্বর',
    // Add more translations as needed
  },
  telugu: {
    'app.title': 'శక్తిసేతు',
    'app.tagline': 'మహిళా నేతృత్వంలోని MSMEs సాధికారత',
    'nav.home': 'హోమ్',
    'nav.marketplace': 'మార్కెట్‌ప్లేస్',
    'nav.storefront': 'స్టోర్‌ఫ్రంట్',
    'nav.procurement': 'ప్రొక్యూర్‌మెంట్',
    'nav.learning': 'లెర్నింగ్',
    'nav.mentorship': 'మెంటర్‌షిప్',
    'nav.schemes': 'ప్రభుత్వ పథకాలు',
    'nav.login': 'లాగిన్',
    'nav.register': 'రిజిస్టర్',
    'auth.email': 'ఇమెయిల్',
    'auth.password': 'పాస్‌వర్డ్',
    'auth.login': 'లాగిన్',
    'auth.register': 'రిజిస్టర్',
    'auth.fullName': 'పూర్తి పేరు',
    'auth.businessName': 'వ్యాపార పేరు',
    'auth.phone': 'ఫోన్ నంబర్',
    // Add more translations as needed
  },
  marathi: {
    'app.title': 'शक्तिसेतू',
    'app.tagline': 'महिला नेतृत्वाखालील MSMEs चे सक्षमीकरण',
    'nav.home': 'होम',
    'nav.marketplace': 'मार्केटप्लेस',
    'nav.storefront': 'स्टोरफ्रंट',
    'nav.procurement': 'प्रोक्युरमेंट',
    'nav.learning': 'लर्निंग',
    'nav.mentorship': 'मेंटरशिप',
    'nav.schemes': 'सरकारी योजना',
    'nav.login': 'लॉगिन',
    'nav.register': 'रजिस्टर',
    'auth.email': 'ईमेल',
    'auth.password': 'पासवर्ड',
    'auth.login': 'लॉगिन',
    'auth.register': 'रजिस्टर',
    'auth.fullName': 'पूर्ण नाव',
    'auth.businessName': 'व्यवसायाचे नाव',
    'auth.phone': 'फोन नंबर',
    // Add more translations as needed
  },
  gujarati: {
    'app.title': 'શક્તિસેતુ',
    'app.tagline': 'મહિલા નેતૃત્વવાળા MSMEs નું સશક્તિકરણ',
    'nav.home': 'હોમ',
    'nav.marketplace': 'માર્કેટપ્લેસ',
    'nav.storefront': 'સ્ટોરફ્રન્ટ',
    'nav.procurement': 'પ્રોક્યોરમેન્ટ',
    'nav.learning': 'લર્નિંગ',
    'nav.mentorship': 'મેન્ટરશિપ',
    'nav.schemes': 'સરકારી યોજનાઓ',
    'nav.login': 'લોગિન',
    'nav.register': 'રજિસ્ટર',
    'auth.email': 'ઈમેઈલ',
    'auth.password': 'પાસવર્ડ',
    'auth.login': 'લોગિન',
    'auth.register': 'રજિસ્ટર',
    'auth.fullName': 'પૂરું નામ',
    'auth.businessName': 'વ્યાપાર નામ',
    'auth.phone': 'ફોન નંબર',
    // Add more translations as needed
  },
};

export function LanguageProvider({ children }: { children: ReactNode }) {
  // Get saved language or default to English
  const savedLanguage = localStorage.getItem('language') as Language;
  const [language, setLanguageState] = useState<Language>(savedLanguage || 'english');

  // Update language and save to localStorage
  const setLanguage = (newLanguage: Language) => {
    setLanguageState(newLanguage);
    localStorage.setItem('language', newLanguage);
  };

  // Translation function
  const t = (key: string): string => {
    return translations[language][key] || key;
  };

  // Set document language attribute
  useEffect(() => {
    document.documentElement.lang = language === 'english' ? 'en' : 
                                   language === 'hindi' ? 'hi' :
                                   language === 'tamil' ? 'ta' :
                                   language === 'bengali' ? 'bn' :
                                   language === 'telugu' ? 'te' :
                                   language === 'marathi' ? 'mr' :
                                   language === 'gujarati' ? 'gu' : 'en';
  }, [language]);

  return (
    <LanguageContext.Provider value={{ language, setLanguage, t }}>
      {children}
    </LanguageContext.Provider>
  );
}

export function useLanguage() {
  const context = useContext(LanguageContext);
  if (context === undefined) {
    throw new Error('useLanguage must be used within a LanguageProvider');
  }
  return context;
}
