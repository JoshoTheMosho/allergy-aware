import { TextField, Button } from '@mui/material';

const SearchIngredients = () => {
    return (
        <div>
            <h2>Search Ingredients and Allergens</h2>
            <TextField label="Search" variant="outlined" />
            <Button variant="contained" color="primary">Search</Button>
        </div>
    );
};

export default SearchIngredients;
