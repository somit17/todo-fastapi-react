import { Button } from 'primereact/button';
import 'primereact/resources/themes/lara-light-indigo/theme.css'; //theme
import 'primereact/resources/primereact.min.css'; //core css
import 'primeicons/primeicons.css'; //icons
import './App.css';

function App() {
  return (
    <div className="App">
      <div className="card">
        <Button
          icon="pi pi-plus"
          className="mr-2"
          label="Increment"
        ></Button>
      </div>
    </div>
  );
}

export default App;