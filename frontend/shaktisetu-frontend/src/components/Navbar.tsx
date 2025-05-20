import React from 'react';
import { useLanguage } from '../hooks/useLanguage';
import { useAuth } from '../hooks/useAuth';
import { Button } from './ui/button';
import LanguageSwitcher from './LanguageSwitcher';
import { Link } from 'react-router-dom';

const Navbar: React.FC = () => {
  const { t } = useLanguage();
  const { isAuthenticated, logout, user } = useAuth();

  return (
    <nav className="bg-white shadow-md py-4">
      <div className="container mx-auto px-4 flex flex-col md:flex-row justify-between items-center">
        <div className="flex items-center mb-4 md:mb-0">
          <Link to="/" className="text-2xl font-bold text-primary">
            {t('app.title')}
          </Link>
          <span className="ml-2 text-sm text-gray-500">{t('app.tagline')}</span>
        </div>

        <div className="flex flex-col md:flex-row items-center gap-4">
          <div className="flex space-x-4">
            <Link to="/" className="text-gray-700 hover:text-primary">
              {t('nav.home')}
            </Link>
            <Link to="/marketplace" className="text-gray-700 hover:text-primary">
              {t('nav.marketplace')}
            </Link>
            <Link to="/storefront" className="text-gray-700 hover:text-primary">
              {t('nav.storefront')}
            </Link>
            <Link to="/procurement" className="text-gray-700 hover:text-primary">
              {t('nav.procurement')}
            </Link>
            <Link to="/learning" className="text-gray-700 hover:text-primary">
              {t('nav.learning')}
            </Link>
            <Link to="/mentorship" className="text-gray-700 hover:text-primary">
              {t('nav.mentorship')}
            </Link>
            <Link to="/schemes" className="text-gray-700 hover:text-primary">
              {t('nav.schemes')}
            </Link>
          </div>

          <div className="flex items-center space-x-4">
            {isAuthenticated ? (
              <>
                <span className="text-sm text-gray-700">
                  {user?.full_name || user?.username}
                </span>
                <Button variant="outline" size="sm" onClick={logout}>
                  {t('nav.logout')}
                </Button>
              </>
            ) : (
              <>
                <Link to="/login">
                  <Button variant="outline" size="sm">
                    {t('nav.login')}
                  </Button>
                </Link>
                <Link to="/register">
                  <Button size="sm">{t('nav.register')}</Button>
                </Link>
              </>
            )}
          </div>
        </div>
      </div>
      
      <div className="container mx-auto px-4 mt-2">
        <LanguageSwitcher />
      </div>
    </nav>
  );
};

export default Navbar;
