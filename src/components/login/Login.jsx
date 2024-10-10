import { Auth } from '@supabase/auth-ui-react';
import { ThemeSupa } from '@supabase/auth-ui-shared';

const LoginForm = ({ supabase }) => {
    return (
        <Auth
            supabaseClient={supabase}
            appearance={{
                theme: ThemeSupa,
            }}
            providers={[]} // To implement ['google', 'azure', 'facebook']
            socialLayout='horizontal'
            redirectTo='/search'
        />
    );
};

export default LoginForm;
