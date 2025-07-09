import React from 'react';

const Navbar = () => {
  return (
    <nav className="bg-blue-600 text-white shadow-lg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="flex items-center">
            <h1 className="text-xl font-bold">Data Dashboard</h1>
          </div>
          <div className="hidden md:block">
            <div className="ml-10 flex items-baseline space-x-4">
              <a href="#" className="hover:bg-blue-700 px-3 py-2 rounded-md text-sm font-medium transition-colors">
                Home
              </a>
              <a href="#" className="hover:bg-blue-700 px-3 py-2 rounded-md text-sm font-medium transition-colors">
                Analytics
              </a>
              <a href="#" className="hover:bg-blue-700 px-3 py-2 rounded-md text-sm font-medium transition-colors">
                Reports
              </a>
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;