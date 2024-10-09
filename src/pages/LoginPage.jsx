import LoginForm from '../components/Login/Login';
import { Container, Box, Typography } from '@mui/material';

const LoginPage = ({ supabase }) => {
    return (
        <Container component="main" maxWidth="xs">
            <Box sx={{ marginTop: 8, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                <Typography variant="h5">Login</Typography>
                <LoginForm supabase={supabase} />
            </Box>
        </Container>
    );
};

export default LoginPage;

