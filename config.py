# config.py
"""
Central configuration for the Vehicle Registration Dashboard.
"""

# Database Configuration
DB_FILE = "vehicle_registrations.duckdb"
TABLE_NAME = "vehicle_registrations"

# EV-related fuel categories
EV_FUELS = ['ELECTRIC', 'ELECTRIC(BOV)']

# Color schemes for consistent visualization
COLOR_SCHEME = {
    'primary': '#1f77b4',
    'ev': '#2ca02c',
    'petrol': '#ff7f0e',
    'diesel': '#d62728',
    'cng': '#9467bd',
    'other': '#8c564b'
}

# Fuel color mapping
FUEL_COLORS = {
    'PETROL': COLOR_SCHEME['petrol'],
    'DIESEL': COLOR_SCHEME['diesel'],
    'ELECTRIC': COLOR_SCHEME['ev'],
    'ELECTRIC(BOV)': COLOR_SCHEME['ev'],
    'CNG': COLOR_SCHEME['cng'],
    'LPG': '#bcbd22',
    'OTHER': COLOR_SCHEME['other']
}

# Cache TTL (time to live) in seconds
CACHE_TTL = 3600  # 1 hour

# Default date range for analysis
DEFAULT_START_YEAR = 2020
DEFAULT_END_YEAR = 2026

# Top N items to show in rankings
TOP_N_STATES = 10
TOP_N_MAKERS = 15

# Page configuration
PAGE_CONFIG = {
    "page_title": "India Vehicle Registration Dashboard",
    "page_icon": "🚗",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}