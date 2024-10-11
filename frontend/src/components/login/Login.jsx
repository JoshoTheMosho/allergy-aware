import { useState } from 'react';
import { TextField, Button, Box, Typography } from '@mui/material';
import config from '../../../config';

const LoginForm = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleLogin = async (e) => {
        e.preventDefault(); // Prevent form submission
        setError('');

        console.log(`${config.backendUrl}`);

        console.log(`${import.meta.env}`);

        const response = await fetch(`${config.backendUrl}/auth/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ "email": email, "password": password }),
        });

        if (!response.ok) {
            setError("Incorrect email or password.");
            return;
        }

        const data = await response.json();

        localStorage.setItem('access_token', data.response.session.access_token);
        localStorage.setItem('refresh_token', data.response.session.refresh_token);

        // Redirect to the search page or handle login success
        window.location.href = '/search'; // Redirect after successful login
    };

    return (
        <Box
            sx={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                maxWidth: 400,
                mx: 'auto',
                p: 2,
                border: '1px solid',
                borderColor: 'grey.400',
                borderRadius: 2,
                boxShadow: 2,
                mt: 5,
            }}
        >
            <Typography variant="h5" component="h1" gutterBottom>
                Login
            </Typography>
            {error && (
                <Typography color="error" variant="body2" gutterBottom>
                    {error}
                </Typography>
            )}
            <form onSubmit={handleLogin} style={{ width: '100%' }}>
                <TextField
                    label="Email"
                    variant="outlined"
                    fullWidth
                    margin="normal"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                />
                <TextField
                    label="Password"
                    type="password"
                    variant="outlined"
                    fullWidth
                    margin="normal"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
                <Button
                    type="submit"
                    variant="contained"
                    color="primary"
                    fullWidth
                    sx={{ mt: 2 }}
                >
                    Login
                </Button>
            </form>
        </Box>
    );
};

export default LoginForm;
