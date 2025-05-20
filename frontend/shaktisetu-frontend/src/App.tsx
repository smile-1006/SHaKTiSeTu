import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './hooks/useAuth';
import { LanguageProvider } from './hooks/useLanguage';
import HomePage from './pages/HomePage';

function App() {
  return (
    <LanguageProvider>
      <AuthProvider>
        <Router>
          <Routes>
            <Route path="/" element={<HomePage />} />
            {/* Add more routes as they are implemented */}
            {/* <Route path="/marketplace" element={<MarketplacePage />} /> */}
            {/* <Route path="/storefront" element={<StorefrontPage />} /> */}
            {/* <Route path="/procurement" element={<ProcurementPage />} /> */}
            {/* <Route path="/learning" element={<LearningPage />} /> */}
            {/* <Route path="/mentorship" element={<MentorshipPage />} /> */}
            {/* <Route path="/schemes" element={<SchemesPage />} /> */}
            {/* <Route path="/news" element={<NewsPage />} /> */}
            {/* <Route path="/login" element={<LoginPage />} /> */}
            {/* <Route path="/register" element={<RegisterPage />} /> */}
          </Routes>
        </Router>
      </AuthProvider>
    </LanguageProvider>
  );
}

export default App;
