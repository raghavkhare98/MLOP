import './App.css';
import ResponsiveAppBar from './ResponsiveAppBar';
import ActionAreaCard from './ActionAreaCard';
import { useEffect } from 'react';
function App() {
  
  useEffect(() => {
    const interval = setInterval(() => {
      window.location.reload();
    }, 7000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="App">
      <ResponsiveAppBar />
      <ActionAreaCard />
    </div>
  );
}

export default App;
