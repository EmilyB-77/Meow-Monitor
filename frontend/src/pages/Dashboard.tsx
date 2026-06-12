import React from 'react';

const Dashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div className="bg-white rounded-lg shadow p-6">
        <h1 className="text-3xl font-bold text-gray-900 mb-4">🐱 Meow Monitor</h1>
        <p className="text-gray-600 mb-4">
          Welcome to Meow Monitor! Track your cats' health, feeding schedules, and mood patterns.
        </p>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="bg-blue-50 p-4 rounded-lg">
            <h3 className="font-semibold text-blue-900 mb-2">🏥 Health Tracking</h3>
            <p className="text-sm text-blue-700">Monitor vaccinations, checkups, and medical records</p>
          </div>
          <div className="bg-green-50 p-4 rounded-lg">
            <h3 className="font-semibold text-green-900 mb-2">🍽️ Feeding Schedule</h3>
            <p className="text-sm text-green-700">Track meal times and portions</p>
          </div>
          <div className="bg-purple-50 p-4 rounded-lg">
            <h3 className="font-semibold text-purple-900 mb-2">😸 Mood Tracking</h3>
            <p className="text-sm text-purple-700">Log behavioral patterns and emotions</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;