import { TextField, Button } from '@mui/material';

const EditData = () => {
    return (
        <div>
            <h2>Edit Ingredient or Allergen</h2>
            <TextField label="Ingredient/Allergen" variant="outlined" />
            <Button variant="contained" color="primary">Save Changes</Button>
        </div>
    );
};

export default EditData;
