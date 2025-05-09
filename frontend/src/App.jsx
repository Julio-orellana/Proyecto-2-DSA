import { useEffect, useState } from 'react';
import { fetchData } from './services/api';

function App() {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetchData().then(setData).catch(console.error);
    }, []);

    return (
        <div>
            <h1>Datos desde Flask:</h1>
            <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
    );
}

export default App;