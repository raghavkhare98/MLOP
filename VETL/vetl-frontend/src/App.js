import './App.css';
import Navbar from './components/Navbar';
import DataTable from './components/DataTable';
import GraphsSection from './components/GraphSection';

function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />
      
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <DataTable />
        <GraphsSection />
      </main>
    </div>
  );
}

export default App;
