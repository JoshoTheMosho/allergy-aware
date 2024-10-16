import { useState, useEffect } from 'react';
import axios from 'axios';
import SearchIngredients from '../components/searchIngredients/SearchIngredients';
import { Grid2, Card, CardContent, Typography } from '@mui/material';
import config from '../../config';
import NotLoggedIn from '../components/common/NotLoggedIn';

const SearchPage = () => {
    const [results, setResults] = useState([]);
    const [token, setToken] = useState('');
    const [loading, setLoading] = useState(false);
    const [hasSearched, setHasSearched] = useState(false);

    // Hardcode the token you retrieved from Postman
    //const token = 'Bearer token';


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

        setResults([]);
        setLoading(true);
        setHasSearched(true);

        try {
            const response = await axios.get(`${config.backendUrl}/allergens/search/`, {
                headers: {
                    Authorization: `Bearer ${token}` //token
                },
                params: {
                    query: query
                }
            });

            // Set the search results in the state
            setResults(response.data);
        } catch (err) {
            console.error('An error occurred while fetching data:', err);
        } finally {
            setLoading(false);
        }
    };

    if (!localStorage.getItem('access_token')) {
        return <NotLoggedIn />;
    }

    return (
        <div>
            <SearchIngredients onSearch={handleSearch} loading={loading} />
            {/* Display search results */}
            <div style={{ marginTop: '20px' }}>
                {results.length > 0 ? (
                    <Grid2 container spacing={2}>
                        {results.map((result, index) => (
                            <Grid2 item xs={12} sm={6} md={4} key={`${result.name}-${result.ingredient}-${index}`}>
                                <Card style={{ backgroundColor: '#f5f5f5', borderRadius: '8px' }}>
                                    <CardContent>
                                        <Typography variant="h6" component="div">
                                            {result.name}
                                        </Typography>
                                        <Typography variant="body2" color="textSecondary">
                                            Ingredient: {result.ingredient}
                                        </Typography>
                                    </CardContent>
                                </Card>
                            </Grid2>
                        ))}
                    </Grid2>
                ) : (
                    hasSearched && !loading && (
                        <Typography variant="body1" color="textSecondary" style={{ textAlign: 'center', marginTop: '20px' }}>
                            No results found.
                        </Typography>
                    )
                )}
            </div>
        </div>
    );
};

//const SearchPage = ({ supabase }) => <SearchIngredients />;

export default SearchPage;
