import { useState, useEffect } from 'react';
import axios from 'axios';
import SearchIngredients from '../components/searchIngredients/SearchIngredients';

const SearchPage = ({ supabase }) => {
    const [results, setResults] = useState([]);
    const [token, setToken] = useState('');

    useEffect(() => {
        // Example: Fetch and set the auth token from Supabase or localStorage if logged in
        // Replace with actual implementation based on how your authentication works
        const fetchAuthToken = async () => {
            // Assuming token is stored in localStorage after login
            const authToken = localStorage.getItem('access_token');
            if (authToken) {
                setToken(authToken);
            } else {
                console.error("No token found");
            }
        };

        fetchAuthToken();
    }, []);

    // Function to perform search using your backend API
    const handleSearch = async (query) => {
        if (!token) {
            console.error('User is not authenticated');
            return;
        }

        try {
            const response = await axios.get(`http://localhost:8000/api/search/`, {
                headers: {
                    Authorization: `Bearer ${token}`
                },
                params: {
                    query: query
                }
            });

            // Set the search results in the state
            setResults(response.data);
        } catch (err) {
            console.error('An error occurred while fetching data:', err);
        }
    };

    return (
        <div>
            <SearchIngredients onSearch={handleSearch} />
            {/* Display search results */}
            <div>
                {results.length > 0 ? (
                    <ul>
                        {results.map((result) => (
                            <li key={result.id}>
                                {result.ingredient_name} - {result.allergen}
                            </li>
                        ))}
                    </ul>
                ) : (
                    <p>No results found.</p>
                )}
            </div>
        </div>
    );
};

//const SearchPage = ({ supabase }) => <SearchIngredients />;

export default SearchPage;
