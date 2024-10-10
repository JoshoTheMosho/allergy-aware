"""
This module configures the connection to the Supabase database.

Environment Variables:
- SUPABASE_URL: The URL of the Supabase project.
- SUPABASE_KEY: The API key for the Supabase project.

Attributes:
- supabase (Client): The Supabase client used to interact with the database.
"""

import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Retrieve the Supabase URL and key from environment variables
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

# Create a Supabase client using the retrieved URL and key
supabase: Client = create_client(url, key)