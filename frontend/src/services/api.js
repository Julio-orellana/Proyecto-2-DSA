export const fetchData = async () => {
    const response = await fetch('/api/data'); 
    if (!response.ok) throw new Error('Error en la API');
    return await response.json();
};