import React from 'react';
import { Link } from 'react-router-dom';

const Header: React.FC = () => {
  return (
    <header className="bg-white shadow">
      <nav className="container mx-auto px-4 py-4 flex justify-between items-center">
        <Link to="/" className="text-2xl font-bold text-purple-600">
          🐱 Meow Monitor
        </Link>
        <ul className="flex gap-6">
          <li><Link to="/" className="text-gray-600 hover:text-gray-900">Dashboard</Link></li>
          <li><Link to="/cats" className="text-gray-600 hover:text-gray-900">My Cats</Link></li>
          <li><Link to="/profile" className="text-gray-600 hover:text-gray-900">Profile</Link></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;