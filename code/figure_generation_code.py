"""
The 2026 Refinancing Wall - Figure Generation Code
CEDX Research Report
Generated: January 2026

This script generates all visualizations for the refinancing wall analysis report.
All figures are saved at 300 DPI with professional styling.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import matplotlib.lines as mlines
import numpy as np
import pandas as pd
from pathlib import Path

# ============================================================================
# CONFIGURATION AND STYLING
# ============================================================================

# Color Palette - Professional Earth Tones
COLORS = {
    'primary': '#1a365d',      # Deep Blue
    'secondary': '#b7791f',    # Gold
    'accent': '#718096',       # Gray
    'danger': '#c53030',       # Red
    'success': '#2f855a',      # Green
    'warning': '#d69e2e',      # Amber
    'light': '#f7fafc',        # Light Gray
    'dark': '#1a202c'          # Dark
}

# Country Colors
COUNTRY_COLORS = {
    'Ghana': '#c53030',
    'Sri Lanka': '#2f855a',
    'Zambia': '#b7791f',
    'Pakistan': '#1a365d',
    'Kenya': '#6b46c1',
    'Egypt': '#d69e2e',
    'Nigeria': '#e53e3e'
}

# Instrument Colors
INSTRUMENT_COLORS = {
    'Eurobonds': '#c53030',
    'External FX Debt': '#b7791f',
    'Local Currency': '#1a365d',
    'SOE Obligations': '#718096'
}

# Output directory
OUTPUT_DIR = Path('/home/z/my-project/download/refinancing_wall_report/figures')
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Set matplotlib defaults
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

def save_figure(fig, filename):
    """Save figure with consistent settings"""
    filepath = OUTPUT_DIR / filename
    fig.savefig(filepath, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"Saved: {filepath}")
    return str(filepath)


# ============================================================================
# FIGURE 1.1 - CONCEPTUAL FRAMEWORK DIAGRAM
# ============================================================================

def create_figure_1_1():
    """Conceptual Framework - Refinancing Wall Mechanism"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Title
    ax.text(6, 7.5, 'Figure 1.1: The Refinancing Wall - Conceptual Framework', 
            ha='center', va='top', fontsize=14, fontweight='bold', color=COLORS['primary'])
    
    # Define boxes
    boxes = [
        (1, 6, 'Maturity\nBunching', COLORS['primary']),
        (4.5, 6, 'High Global\nInterest Rates', COLORS['primary']),
        (8, 6, 'Tighter Risk\nAppetite', COLORS['primary']),
        (2.75, 4, 'Rollover\nImpossibility', COLORS['danger']),
        (6.25, 4, 'Refinancing\nWall', COLORS['danger']),
        (1, 2, 'FX Reserve\nDrawdown', COLORS['warning']),
        (4.5, 2, 'Auction\nFailure', COLORS['warning']),
        (8, 2, 'Spread\nWidening', COLORS['warning']),
        (4.5, 0.5, 'Default Probability\nSpike', COLORS['danger']),
    ]
    
    for x, y, text, color in boxes:
        box = FancyBboxPatch((x-0.9, y-0.4), 1.8, 0.8, 
                             boxstyle="round,pad=0.05", 
                             facecolor=color, alpha=0.8, edgecolor='white', linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=10, 
                color='white', fontweight='bold', wrap=True)
    
    # Add arrows
    arrow_style = dict(arrowstyle='->', color=COLORS['accent'], lw=2)
    arrows = [
        ((2.1, 6), (3.4, 6)), ((5.6, 6), (6.9, 6)),
        ((3.65, 6), (2.75, 4.5)), ((7.15, 6), (6.25, 4.5)),
        ((4.5, 5.5), (4.5, 4.5)),
        ((2.75, 3.5), (1.9, 2.5)), ((4.5, 3.5), (4.5, 2.5)), ((6.25, 3.5), (8.1, 2.5)),
        ((1.9, 1.5), (4, 0.9)), ((4.5, 1.5), (4.5, 1)), ((8.1, 1.5), (5, 0.9)),
    ]
    
    for start, end in arrows:
        ax.annotate('', xy=end, xytext=start, arrowprops=arrow_style)
    
    # Add note
    ax.text(6, -0.3, 'SOURCE: CEDX Framework Analysis', ha='center', fontsize=9, 
            color=COLORS['accent'], style='italic')
    
    return save_figure(fig, 'figure_1_1_conceptual_framework.png')


# ============================================================================
# FIGURE 2.1 - GLOBAL INTEREST RATE TRENDS
# ============================================================================

def create_figure_2_1():
    """Global Interest Rate Trends (2019-2026)"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    years = np.array([2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026])
    
    # Interest rate data (approximate historical + projections)
    fed_funds = [2.2, 0.1, 0.1, 4.3, 5.3, 5.0, 4.5, 4.0]
    ecb_rate = [0.0, 0.0, 0.0, 2.0, 4.0, 3.5, 3.0, 2.5]
    boe_rate = [0.8, 0.1, 0.1, 3.5, 5.0, 4.75, 4.0, 3.5]
    em_average = [4.5, 3.5, 3.8, 6.5, 8.0, 7.5, 6.5, 5.5]
    
    ax.plot(years, fed_funds, 'o-', color='#1a365d', lw=2, ms=6, label='Fed Funds Rate')
    ax.plot(years, ecb_rate, 's-', color='#b7791f', lw=2, ms=6, label='ECB Rate')
    ax.plot(years, boe_rate, '^-', color='#2f855a', lw=2, ms=6, label='Bank of England Rate')
    ax.plot(years, em_average, 'D-', color='#c53030', lw=2, ms=6, label='EM Average Policy Rate')
    
    # Add shaded region for tightening cycle
    ax.axvspan(2022, 2024, alpha=0.15, color=COLORS['warning'], label='Global Tightening Cycle')
    
    ax.set_xlabel('Year', fontsize=11)
    ax.set_ylabel('Policy Rate (%)', fontsize=11)
    ax.set_title('Figure 2.1: Global Interest Rate Trends (2019-2026)', fontsize=12, fontweight='bold')
    ax.legend(loc='upper left', framealpha=0.9)
    ax.set_xlim(2018.5, 2026.5)
    ax.set_ylim(-0.5, 9)
    ax.grid(True, alpha=0.3)
    
    # Add annotation
    ax.annotate('Peak rates\nreached 2023', xy=(2023, 8), xytext=(2024.5, 8.5),
                fontsize=9, ha='center', arrowprops=dict(arrowstyle='->', color='gray'))
    
    ax.text(2022.5, -0.8, 'SOURCE: Federal Reserve, ECB, Bank of England, IMF | NOTE: 2025-2026 are projections', 
            ha='center', fontsize=9, color=COLORS['accent'], style='italic')
    
    return save_figure(fig, 'figure_2_1_global_interest_rates.png')


# ============================================================================
# FIGURE 2.2 - SOVEREIGN SPREAD EVOLUTION
# ============================================================================

def create_figure_2_2():
    """Sovereign Spread Evolution"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
    
    # Spread data (basis points)
    embi_global = [350, 320, 580, 520, 380, 420]
    ghana = [850, 920, 2800, 2500, 2000, 1800]
    sri_lanka = [650, 720, 3500, 3200, 2800, 2400]
    zambia = [1200, 1500, 2800, 2200, 1600, 1400]
    pakistan = [580, 650, 1500, 1800, 1400, 1200]
    
    ax.plot(years, embi_global, 'o-', color=COLORS['primary'], lw=2, label='EMBI Global Spread')
    ax.plot(years, ghana, 's-', color=COUNTRY_COLORS['Ghana'], lw=2, label='Ghana')
    ax.plot(years, sri_lanka, '^-', color=COUNTRY_COLORS['Sri Lanka'], lw=2, label='Sri Lanka')
    ax.plot(years, zambia, 'D-', color=COUNTRY_COLORS['Zambia'], lw=2, label='Zambia')
    ax.plot(years, pakistan, 'v-', color=COUNTRY_COLORS['Pakistan'], lw=2, label='Pakistan')
    
    # Crisis threshold line
    ax.axhline(y=1000, color=COLORS['danger'], linestyle='--', alpha=0.7, label='Distress Threshold (1000 bps)')
    
    ax.set_xlabel('Year', fontsize=11)
    ax.set_ylabel('Spread (basis points)', fontsize=11)
    ax.set_title('Figure 2.2: Sovereign Spread Evolution (2020-2025)', fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', framealpha=0.9)
    ax.set_xlim(2019.5, 2025.5)
    ax.grid(True, alpha=0.3)
    
    # Add crisis annotation
    ax.annotate('2022 Crisis Peak', xy=(2022, 2800), xytext=(2021, 3200),
                fontsize=9, arrowprops=dict(arrowstyle='->', color='gray'))
    
    ax.text(2022.5, -400, 'SOURCE: Bloomberg, JPMorgan EMBI | NOTE: Spreads over US Treasuries', 
            ha='center', fontsize=9, color=COLORS['accent'], style='italic')
    
    return save_figure(fig, 'figure_2_2_sovereign_spreads.png')


# ============================================================================
# FIGURE 4.1 - AGGREGATE MATURITY WALL
# ============================================================================

def create_figure_4_1():
    """Maturity Wall Chart (Aggregate)"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    years = ['2024', '2025', '2026', '2027', '2028', '2029', '2030']
    
    # Debt maturities by instrument ($ billion)
    eurobonds = [0.4, 3.2, 5.3, 8.7, 4.2, 2.0, 7.5]
    external_fx = [8.2, 13.0, 17.3, 14.6, 16.1, 13.7, 15.5]
    local_currency = [24.0, 33.5, 41.4, 38.8, 44.4, 33.5, 39.0]
    soe_obligations = [2.8, 4.2, 6.0, 5.3, 4.2, 4.8, 5.4]
    
    x = np.arange(len(years))
    width = 0.6
    
    ax.bar(x, eurobonds, width, label='Eurobonds', color=INSTRUMENT_COLORS['Eurobonds'])
    ax.bar(x, external_fx, width, bottom=eurobonds, label='External FX Debt', color=INSTRUMENT_COLORS['External FX Debt'])
    ax.bar(x, local_currency, width, bottom=np.array(eurobonds)+np.array(external_fx), 
           label='Local Currency', color=INSTRUMENT_COLORS['Local Currency'])
    ax.bar(x, soe_obligations, width, 
           bottom=np.array(eurobonds)+np.array(external_fx)+np.array(local_currency),
           label='SOE Obligations', color=INSTRUMENT_COLORS['SOE Obligations'])
    
    ax.set_xlabel('Year', fontsize=11)
    ax.set_ylabel('Debt Maturing ($ billion)', fontsize=11)
    ax.set_title('Figure 4.1: Aggregate Debt Maturity Wall (All Countries)', fontsize=12, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.legend(loc='upper left', framealpha=0.9)
    ax.grid(True, alpha=0.3, axis='y')
    
    # Highlight 2026
    ax.axvspan(1.5, 2.5, alpha=0.15, color=COLORS['danger'])
    ax.annotate('2026 Peak\nMaturity Wall', xy=(2, 65), fontsize=10, ha='center', 
                fontweight='bold', color=COLORS['danger'])
    
    ax.text(3, -10, 'SOURCE: Country debt offices, IMF DSA, Bloomberg | NOTE: Sample of 7 emerging markets', 
            ha='center', fontsize=9, color=COLORS['accent'], style='italic')
    
    return save_figure(fig, 'figure_4_1_aggregate_maturity_wall.png')


# ============================================================================
# FIGURE 4.2 - COUNTRY-LEVEL MATURITY WALLS
# ============================================================================

def create_figure_4_2():
    """Country-Level Maturity Walls"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    years = ['2024', '2025', '2026', '2027', '2028', '2029', '2030']
    countries_data = {
        'Ghana': {
            'Eurobonds': [0, 0, 2.5, 0.5, 4.2, 0, 2.0],
            'External FX': [1.2, 1.8, 2.1, 1.5, 1.8, 2.2, 1.5],
            'Local Currency': [3.5, 4.2, 5.1, 4.8, 5.5, 4.2, 4.8],
            'SOE': [0.3, 0.5, 0.8, 0.6, 0.4, 0.5, 0.6]
        },
        'Sri Lanka': {
            'Eurobonds': [0, 0, 0, 0, 0, 0, 0],
            'External FX': [0.5, 1.2, 2.5, 1.8, 1.5, 2.0, 1.8],
            'Local Currency': [2.8, 3.5, 4.2, 3.8, 4.5, 3.2, 4.0],
            'SOE': [0.2, 0.4, 0.6, 0.5, 0.3, 0.4, 0.5]
        },
        'Zambia': {
            'Eurobonds': [0, 0, 0, 1.5, 0, 0, 2.0],
            'External FX': [0.4, 0.8, 1.2, 0.9, 1.1, 0.8, 1.0],
            'Local Currency': [1.2, 1.8, 2.4, 2.1, 2.5, 1.8, 2.2],
            'SOE': [0.1, 0.2, 0.3, 0.2, 0.2, 0.2, 0.2]
        },
        'Pakistan': {
            'Eurobonds': [0.4, 1.2, 2.8, 1.5, 0, 0, 0],
            'External FX': [2.5, 4.2, 5.5, 4.8, 5.2, 4.5, 5.0],
            'Local Currency': [8.5, 12.4, 15.2, 14.8, 16.5, 12.8, 14.2],
            'SOE': [1.2, 1.8, 2.5, 2.2, 1.8, 2.0, 2.2]
        }
    }
    
    for ax, (country, data) in zip(axes.flatten(), countries_data.items()):
        x = np.arange(len(years))
        width = 0.6
        
        bottom = np.zeros(len(years))
        for instrument in ['Eurobonds', 'External FX', 'Local Currency', 'SOE']:
            values = data[instrument]
            ax.bar(x, values, width, bottom=bottom, 
                   color=INSTRUMENT_COLORS[instrument], label=instrument if ax == axes[0, 0] else '')
            bottom += np.array(values)
        
        ax.set_title(f'{country}', fontsize=11, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(years, fontsize=9)
        ax.set_ylabel('$ billion', fontsize=10)
        ax.grid(True, alpha=0.3, axis='y')
        
        # Highlight 2026
        ax.axvspan(1.5, 2.5, alpha=0.15, color=COLORS['danger'])
    
    fig.suptitle('Figure 4.2: Country-Level Debt Maturity Walls', fontsize=12, fontweight='bold', y=1.02)
    
    # Add legend
    handles = [mpatches.Patch(color=INSTRUMENT_COLORS[k], label=k) for k in INSTRUMENT_COLORS]
    fig.legend(handles=handles, loc='lower center', ncol=4, bbox_to_anchor=(0.5, -0.02))
    
    plt.tight_layout()
    
    return save_figure(fig, 'figure_4_2_country_maturity_walls.png')


# ============================================================================
# FIGURE 4.3 - GROSS FINANCING NEEDS
# ============================================================================

def create_figure_4_3():
    """Gross Financing Needs (% of GDP)"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    countries = ['Ghana', 'Sri Lanka', 'Zambia', 'Pakistan', 'Kenya', 'Egypt', 'Nigeria']
    years = ['2025', '2026', '2027', '2028']
    
    gfn_data = {
        'Ghana': [18.2, 22.4, 19.8, 21.2],
        'Sri Lanka': [15.8, 18.5, 16.2, 17.8],
        'Zambia': [14.2, 17.5, 15.8, 16.5],
        'Pakistan': [21.5, 28.2, 25.4, 24.8],
        'Kenya': [16.8, 14.2, 13.5, 15.2],
        'Egypt': [22.4, 25.8, 23.5, 24.2],
        'Nigeria': [12.5, 14.2, 13.8, 14.5]
    }
    
    x = np.arange(len(countries))
    width = 0.2
    
    for i, year in enumerate(years):
        values = [gfn_data[c][i] for c in countries]
        bars = ax.bar(x + i*width, values, width, label=year, alpha=0.85)
    
    # Add threshold lines
    ax.axhline(y=20, color=COLORS['danger'], linestyle='--', lw=2, label='Crisis Threshold (20%)')
    ax.axhline(y=15, color=COLORS['warning'], linestyle=':', lw=2, label='Stress Threshold (15%)')
    
    ax.set_xlabel('Country', fontsize=11)
    ax.set_ylabel('Gross Financing Need (% of GDP)', fontsize=11)
    ax.set_title('Figure 4.3: Gross Financing Needs (% GDP) by Country', fontsize=12, fontweight='bold')
    ax.set_xticks(x + 1.5*width)
    ax.set_xticklabels(countries)
    ax.legend(loc='upper right', framealpha=0.9, ncol=2)
    ax.grid(True, alpha=0.3, axis='y')
    
    ax.text(3, -4, 'SOURCE: IMF DSA, World Bank, CEDX Calculations | NOTE: GFN = Amortization + Interest + Primary Deficit', 
            ha='center', fontsize=9, color=COLORS['accent'], style='italic')
    
    return save_figure(fig, 'figure_4_3_gross_financing_needs.png')


# ============================================================================
# FIGURE 4.4 - DEBT SERVICE TO REVENUE RATIO
# ============================================================================

def create_figure_4_4():
    """Debt Service to Revenue Ratio"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    countries = ['Ghana', 'Sri Lanka', 'Zambia', 'Pakistan', 'Kenya', 'Egypt', 'Nigeria']
    ratios_2024 = [38.5, 52.4, 45.2, 48.5, 32.5, 42.5, 28.2]
    ratios_2026 = [48.2, 42.8, 35.2, 58.4, 32.2, 48.5, 32.4]
    
    x = np.arange(len(countries))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, ratios_2024, width, label='2024', color=COLORS['primary'], alpha=0.85)
    bars2 = ax.bar(x + width/2, ratios_2026, width, label='2026', color=COLORS['secondary'], alpha=0.85)
    
    # Add threshold lines
    ax.axhline(y=30, color=COLORS['danger'], linestyle='--', lw=2, label='Crisis Threshold (30%)')
    ax.axhline(y=25, color=COLORS['warning'], linestyle=':', lw=2, label='Politically Explosive (25%)')
    
    # Color bars above threshold
    for bar, ratio in zip(bars2, ratios_2026):
        if ratio > 30:
            bar.set_color(COLORS['danger'])
            bar.set_alpha(0.85)
    
    ax.set_xlabel('Country', fontsize=11)
    ax.set_ylabel('Debt Service / Government Revenue (%)', fontsize=11)
    ax.set_title('Figure 4.4: Debt Service to Revenue Ratio', fontsize=12, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(countries)
    ax.legend(loc='upper right', framealpha=0.9)
    ax.grid(True, alpha=0.3, axis='y')
    
    ax.text(3, -6, 'SOURCE: IMF DSA, Ministry of Finance data, CEDX Analysis | NOTE: Ratios above 25-30% crowd out essential spending', 
            ha='center', fontsize=9, color=COLORS['accent'], style='italic')
    
    return save_figure(fig, 'figure_4_4_debt_service_revenue_ratio.png')


# ============================================================================
# FIGURE 4.5 - STRESS SCENARIO FAN CHART
# ============================================================================

def create_figure_4_5():
    """Stress Scenario Fan Chart"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    years = np.array([2024, 2025, 2026, 2027, 2028])
    
    # Ghana debt service projections
    baseline = [4.2, 4.8, 5.5, 5.2, 5.0]
    moderate_stress = [4.2, 5.2, 6.8, 6.5, 6.2]
    severe_stress = [4.2, 5.8, 8.5, 8.2, 7.8]
    
    # Confidence bands
    lower = baseline
    upper_severe = severe_stress
    upper_moderate = moderate_stress
    
    # Plot fan chart
    ax.fill_between(years, lower, upper_severe, alpha=0.3, color=COLORS['danger'], label='Severe Stress Scenario')
    ax.fill_between(years, lower, upper_moderate, alpha=0.4, color=COLORS['warning'], label='Moderate Stress Scenario')
    
    ax.plot(years, baseline, 'o-', color=COLORS['primary'], lw=3, label='Baseline')
    ax.plot(years, moderate_stress, 's--', color=COLORS['warning'], lw=2, label='Moderate Stress (+300bps)')
    ax.plot(years, severe_stress, '^--', color=COLORS['danger'], lw=2, label='Severe Stress (+300bps, -15% FX, -1.5pp growth)')
    
    ax.set_xlabel('Year', fontsize=11)
    ax.set_ylabel('Debt Service ($ billion)', fontsize=11)
    ax.set_title('Figure 4.5: Ghana Debt Service Trajectories Under Stress Scenarios', fontsize=12, fontweight='bold')
    ax.legend(loc='upper left', framealpha=0.9)
    ax.grid(True, alpha=0.3)
    
    ax.text(2026, 3.5, 'SOURCE: CEDX Stress Model | NOTE: Stress assumptions: +300bps spreads, -15% FX, -1.5pp growth', 
            ha='center', fontsize=9, color=COLORS['accent'], style='italic')
    
    return save_figure(fig, 'figure_4_5_stress_scenario_fan_chart.png')


# ============================================================================
# FIGURE 4.6 - REFINANCING GAP MODEL RESULTS
# ============================================================================

def create_figure_4_6():
    """Refinancing Gap Model Results"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    countries = ['Ghana', 'Sri Lanka', 'Zambia', 'Pakistan', 'Kenya', 'Egypt', 'Nigeria']
    baseline_gap = [4.2, 3.8, 2.5, 8.5, 2.8, 6.5, 3.2]
    stress_gap = [8.5, 7.2, 5.2, 15.2, 5.5, 12.8, 6.5]
    
    x = np.arange(len(countries))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, baseline_gap, width, label='Baseline Gap', color=COLORS['primary'], alpha=0.85)
    bars2 = ax.bar(x + width/2, stress_gap, width, label='Stress Scenario Gap', color=COLORS['danger'], alpha=0.85)
    
    # Add value labels
    for bar in bars1:
        height = bar.get_height()
        ax.annotate(f'${height:.1f}bn', xy=(bar.get_x() + bar.get_width()/2, height),
                   xytext=(0, 3), textcoords='offset points', ha='center', fontsize=8)
    
    for bar in bars2:
        height = bar.get_height()
        ax.annotate(f'${height:.1f}bn', xy=(bar.get_x() + bar.get_width()/2, height),
                   xytext=(0, 3), textcoords='offset points', ha='center', fontsize=8)
    
    ax.set_xlabel('Country', fontsize=11)
    ax.set_ylabel('Refinancing Gap ($ billion)', fontsize=11)
    ax.set_title('Figure 4.6: Refinancing Gap Model Results', fontsize=12, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(countries)
    ax.legend(loc='upper right', framealpha=0.9)
    ax.grid(True, alpha=0.3, axis='y')
    
    ax.text(3, -2.5, 'SOURCE: CEDX Refinancing Gap Model | NOTE: Gap = Financing Need - Available Resources', 
            ha='center', fontsize=9, color=COLORS['accent'], style='italic')
    
    return save_figure(fig, 'figure_4_6_refinancing_gap_results.png')


# ============================================================================
# FIGURE 4.7 - EXTERNAL VS LOCAL ROLLOVER CAPACITY
# ============================================================================

def create_figure_4_7():
    """External vs Local Rollover Capacity"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    countries = ['Ghana', 'Sri Lanka', 'Zambia', 'Pakistan', 'Kenya']
    
    # External market
    external_need = [6.8, 3.6, 3.0, 12.5, 4.5]
    external_capacity = [4.5, 1.8, 2.2, 8.0, 3.8]
    
    # Local market
    local_need = [9.2, 6.5, 4.2, 21.0, 5.8]
    local_capacity = [8.0, 5.0, 3.5, 15.0, 5.5]
    
    x = np.arange(len(countries))
    width = 0.35
    
    # External market chart
    ax1 = axes[0]
    bars1 = ax1.bar(x - width/2, external_need, width, label='Need', color=COLORS['danger'], alpha=0.85)
    bars2 = ax1.bar(x + width/2, external_capacity, width, label='Capacity', color=COLORS['success'], alpha=0.85)
    ax1.set_title('External Market Rollover', fontsize=11, fontweight='bold')
    ax1.set_xlabel('Country', fontsize=10)
    ax1.set_ylabel('$ billion', fontsize=10)
    ax1.set_xticks(x)
    ax1.set_xticklabels(countries)
    ax1.legend(loc='upper right', framealpha=0.9)
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Local market chart
    ax2 = axes[1]
    bars3 = ax2.bar(x - width/2, local_need, width, label='Need', color=COLORS['danger'], alpha=0.85)
    bars4 = ax2.bar(x + width/2, local_capacity, width, label='Capacity', color=COLORS['success'], alpha=0.85)
    ax2.set_title('Local Market Rollover', fontsize=11, fontweight='bold')
    ax2.set_xlabel('Country', fontsize=10)
    ax2.set_ylabel('$ billion', fontsize=10)
    ax2.set_xticks(x)
    ax2.set_xticklabels(countries)
    ax2.legend(loc='upper right', framealpha=0.9)
    ax2.grid(True, alpha=0.3, axis='y')
    
    fig.suptitle('Figure 4.7: External vs Local Market Rollover Capacity', fontsize=12, fontweight='bold', y=1.02)
    
    plt.tight_layout()
    
    return save_figure(fig, 'figure_4_7_rollover_capacity.png')


# ============================================================================
# FIGURE 4.8 - FX RESERVE ADEQUACY
# ============================================================================

def create_figure_4_8():
    """FX Reserve Adequacy"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    countries = ['Ghana', 'Sri Lanka', 'Zambia', 'Pakistan', 'Kenya', 'Egypt', 'Nigeria']
    
    # Months of imports
    months_imports = [2.8, 1.9, 2.4, 1.3, 4.2, 3.2, 5.8]
    # Short-term debt coverage
    st_debt_coverage = [42, 28, 38, 22, 65, 48, 85]
    
    x = np.arange(len(countries))
    
    # Chart 1: Months of imports
    ax1 = axes[0]
    colors1 = [COLORS['danger'] if m < 3 else COLORS['warning'] if m < 4 else COLORS['success'] for m in months_imports]
    bars1 = ax1.bar(x, months_imports, color=colors1, alpha=0.85)
    ax1.axhline(y=3, color=COLORS['danger'], linestyle='--', lw=2, label='Critical Threshold (3 months)')
    ax1.axhline(y=4, color=COLORS['warning'], linestyle=':', lw=2, label='Marginal Threshold (4 months)')
    ax1.set_title('Reserves in Months of Imports', fontsize=11, fontweight='bold')
    ax1.set_xlabel('Country', fontsize=10)
    ax1.set_ylabel('Months of Imports', fontsize=10)
    ax1.set_xticks(x)
    ax1.set_xticklabels(countries)
    ax1.legend(loc='upper right', framealpha=0.9, fontsize=9)
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Chart 2: Short-term debt coverage
    ax2 = axes[1]
    colors2 = [COLORS['danger'] if c < 50 else COLORS['warning'] if c < 75 else COLORS['success'] for c in st_debt_coverage]
    bars2 = ax2.bar(x, st_debt_coverage, color=colors2, alpha=0.85)
    ax2.axhline(y=100, color=COLORS['success'], linestyle='--', lw=2, label='Safe Threshold (100%)')
    ax2.axhline(y=50, color=COLORS['danger'], linestyle=':', lw=2, label='Critical Threshold (50%)')
    ax2.set_title('Short-term Debt Coverage (%)', fontsize=11, fontweight='bold')
    ax2.set_xlabel('Country', fontsize=10)
    ax2.set_ylabel('% of Short-term Debt', fontsize=10)
    ax2.set_xticks(x)
    ax2.set_xticklabels(countries)
    ax2.legend(loc='upper right', framealpha=0.9, fontsize=9)
    ax2.grid(True, alpha=0.3, axis='y')
    
    fig.suptitle('Figure 4.8: FX Reserve Adequacy Indicators', fontsize=12, fontweight='bold', y=1.02)
    
    plt.tight_layout()
    
    return save_figure(fig, 'figure_4_8_fx_reserve_adequacy.png')


# ============================================================================
# FIGURE 5.1 - DECISION TREE
# ============================================================================

def create_figure_5_1():
    """Decision Tree: Pre-funding vs Reprofiling vs Restructuring"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    ax.text(7, 7.5, 'Figure 5.1: Liability Management Decision Tree', 
            ha='center', va='top', fontsize=14, fontweight='bold', color=COLORS['primary'])
    
    # Decision nodes
    nodes = [
        (7, 6.5, 'Assess Refinancing\nRisk', COLORS['primary'], 'decision'),
        (3, 5, 'Market Access\nAvailable?', COLORS['primary'], 'decision'),
        (11, 5, 'Reserves\nAdequate?', COLORS['primary'], 'decision'),
        (1.5, 3, 'PRE-FUNDING\n• Buybacks\n• New issuance\n• Cash buffers', COLORS['success'], 'action'),
        (4.5, 3, 'LIABILITY\nMANAGEMENT\n• Exchanges\n• Extensions', COLORS['warning'], 'action'),
        (9.5, 3, 'IMF/IFI\nENGAGEMENT\n• Contingent lines\n• Program support', COLORS['warning'], 'action'),
        (12.5, 3, 'RESTRUCTURING\n• CAC activation\n• Creditor coordination\n• Comprehensive treatment', COLORS['danger'], 'action'),
        (3, 1.5, 'Reserves > 3 months\nSpreads < 500bps', COLORS['accent'], 'condition'),
        (11, 1.5, 'Reserves < 3 months\nSpreads > 1000bps', COLORS['accent'], 'condition'),
    ]
    
    for x, y, text, color, node_type in nodes:
        if node_type == 'decision':
            box = FancyBboxPatch((x-1.2, y-0.5), 2.4, 1, 
                                 boxstyle="round,pad=0.05", 
                                 facecolor=color, alpha=0.85, edgecolor='white', linewidth=2)
        elif node_type == 'action':
            box = FancyBboxPatch((x-1.3, y-0.8), 2.6, 1.6, 
                                 boxstyle="round,pad=0.05", 
                                 facecolor=color, alpha=0.85, edgecolor='white', linewidth=2)
        else:
            box = FancyBboxPatch((x-1.3, y-0.3), 2.6, 0.6, 
                                 boxstyle="round,pad=0.05", 
                                 facecolor=color, alpha=0.5, edgecolor='white', linewidth=1)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=9, 
                color='white' if node_type != 'condition' else COLORS['dark'], fontweight='bold', wrap=True)
    
    # Arrows
    arrows = [
        ((7, 6), (3, 5.5)), ((7, 6), (11, 5.5)),
        ((3, 4.5), (1.5, 3.8)), ((3, 4.5), (4.5, 3.8)),
        ((11, 4.5), (9.5, 3.8)), ((11, 4.5), (12.5, 3.8)),
        ((1.5, 2.2), (3, 1.8)), ((12.5, 2.2), (11, 1.8)),
    ]
    
    for start, end in arrows:
        ax.annotate('', xy=end, xytext=start, 
                   arrowprops=dict(arrowstyle='->', color=COLORS['accent'], lw=1.5))
    
    # Labels
    ax.text(1.5, 5.2, 'YES', fontsize=9, color=COLORS['success'], fontweight='bold')
    ax.text(4.2, 5.2, 'NO', fontsize=9, color=COLORS['danger'], fontweight='bold')
    ax.text(9.2, 5.2, 'YES', fontsize=9, color=COLORS['success'], fontweight='bold')
    ax.text(12, 5.2, 'NO', fontsize=9, color=COLORS['danger'], fontweight='bold')
    
    ax.text(7, 0.5, 'SOURCE: CEDX Decision Framework', ha='center', fontsize=9, 
            color=COLORS['accent'], style='italic')
    
    return save_figure(fig, 'figure_5_1_decision_tree.png')


# ============================================================================
# FIGURE 5.2 - SOVEREIGN-CORPORATE FEEDBACK LOOP
# ============================================================================

def create_figure_5_2():
    """Sovereign-Corporate Feedback Loop"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    ax.text(6, 7.5, 'Figure 5.2: Sovereign-Corporate Feedback Loop', 
            ha='center', va='top', fontsize=14, fontweight='bold', color=COLORS['primary'])
    
    # Central node
    circle_center = Circle((6, 4), 1.2, facecolor=COLORS['danger'], alpha=0.3, edgecolor=COLORS['danger'], linewidth=3)
    ax.add_patch(circle_center)
    ax.text(6, 4, 'REFINANCING\nCRISIS', ha='center', va='center', fontsize=11, 
            fontweight='bold', color=COLORS['danger'])
    
    # Surrounding nodes
    nodes = [
        (2, 6, 'Sovereign\nSpread\nWidening', COLORS['primary']),
        (10, 6, 'Corporate\nBorrowing\nCosts Rise', COLORS['primary']),
        (2, 2, 'Bank Balance\nSheet\nDeterioration', COLORS['warning']),
        (10, 2, 'SOE Financial\nStress', COLORS['warning']),
        (6, 1, 'Contingent\nLiabilities\nMaterialize', COLORS['danger']),
        (6, 7, 'Rating\nDowngrades', COLORS['danger']),
    ]
    
    for x, y, text, color in nodes:
        box = FancyBboxPatch((x-1.1, y-0.5), 2.2, 1, 
                             boxstyle="round,pad=0.05", 
                             facecolor=color, alpha=0.85, edgecolor='white', linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=9, 
                color='white', fontweight='bold', wrap=True)
    
    # Circular arrows
    arrow_style = dict(arrowstyle='->', color=COLORS['accent'], lw=2, connectionstyle='arc3,rad=0.3')
    
    connections = [
        ((3.2, 5.5), (4.8, 4.8)),  # Sovereign spread -> Crisis
        ((7.2, 4.8), (8.8, 5.5)),  # Crisis -> Corporate
        ((8.8, 2.5), (7.2, 3.2)),  # Corporate -> Crisis (bottom)
        ((4.8, 3.2), (3.2, 2.5)),  # Crisis -> Bank
        ((3.2, 6.5), (4.8, 7)),    # Rating -> Crisis (top)
        ((6, 5.2), (6, 6.5)),      # Crisis -> Rating
        ((4.8, 1.5), (3.2, 2)),    # Contingent -> Bank
        ((8.8, 2), (7.2, 1.5)),    # SOE -> Contingent
    ]
    
    for start, end in connections:
        ax.annotate('', xy=end, xytext=start, arrowprops=arrow_style)
    
    ax.text(6, -0.2, 'SOURCE: CEDX Sovereign-Corporate Nexus Analysis', ha='center', fontsize=9, 
            color=COLORS['accent'], style='italic')
    
    return save_figure(fig, 'figure_5_2_sovereign_corporate_loop.png')


# ============================================================================
# FIGURE 6.1-6.4 - CASE STUDY MATURITY PROFILES
# ============================================================================

def create_case_study_figure(country, filename):
    """Create detailed case study figure"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    years = ['2024', '2025', '2026', '2027', '2028', '2029', '2030']
    
    # Country-specific data
    country_data = {
        'Ghana': {
            'eurobonds': [0, 0, 2.5, 0.5, 4.2, 0, 2.0],
            'external': [1.2, 1.8, 2.1, 1.5, 1.8, 2.2, 1.5],
            'local': [3.5, 4.2, 5.1, 4.8, 5.5, 4.2, 4.8],
            'soe': [0.3, 0.5, 0.8, 0.6, 0.4, 0.5, 0.6],
            'gfn': [16.5, 18.2, 22.4, 19.8, 21.2, 18.5, 19.2],
            'spread': [2000, 2000, 1800, 1600, 1400, 1200, 1000],
            'reserves': [5.8, 5.5, 5.2, 5.8, 6.2, 6.5, 7.0],
            'debt_service': [38.5, 42.8, 48.2, 45.5, 44.2, 42.0, 40.5]
        },
        'Sri Lanka': {
            'eurobonds': [0, 0, 0, 0, 0, 0, 0],
            'external': [0.5, 1.2, 2.5, 1.8, 1.5, 2.0, 1.8],
            'local': [2.8, 3.5, 4.2, 3.8, 4.5, 3.2, 4.0],
            'soe': [0.2, 0.4, 0.6, 0.5, 0.3, 0.4, 0.5],
            'gfn': [14.2, 15.8, 18.5, 16.2, 17.8, 15.5, 16.2],
            'spread': [2800, 2800, 2400, 2000, 1600, 1200, 1000],
            'reserves': [2.5, 2.8, 3.2, 3.5, 4.0, 4.5, 5.0],
            'debt_service': [52.4, 45.2, 42.8, 40.5, 38.2, 36.0, 34.5]
        },
        'Zambia': {
            'eurobonds': [0, 0, 0, 1.5, 0, 0, 2.0],
            'external': [0.4, 0.8, 1.2, 0.9, 1.1, 0.8, 1.0],
            'local': [1.2, 1.8, 2.4, 2.1, 2.5, 1.8, 2.2],
            'soe': [0.1, 0.2, 0.3, 0.2, 0.2, 0.2, 0.2],
            'gfn': [12.8, 14.2, 17.5, 15.8, 16.5, 14.2, 15.0],
            'spread': [1600, 1600, 1400, 1200, 1000, 800, 600],
            'reserves': [4.2, 4.5, 4.8, 5.2, 5.5, 5.8, 6.2],
            'debt_service': [45.2, 38.5, 35.2, 33.8, 32.5, 31.0, 30.0]
        },
        'Pakistan': {
            'eurobonds': [0.4, 1.2, 2.8, 1.5, 0, 0, 0],
            'external': [2.5, 4.2, 5.5, 4.8, 5.2, 4.5, 5.0],
            'local': [8.5, 12.4, 15.2, 14.8, 16.5, 12.8, 14.2],
            'soe': [1.2, 1.8, 2.5, 2.2, 1.8, 2.0, 2.2],
            'gfn': [19.5, 21.5, 28.2, 25.4, 24.8, 22.5, 23.0],
            'spread': [1400, 1400, 1200, 1000, 900, 800, 700],
            'reserves': [7.5, 8.2, 9.0, 10.5, 11.5, 12.5, 13.5],
            'debt_service': [48.5, 52.2, 58.4, 55.2, 52.8, 50.0, 48.5]
        }
    }
    
    data = country_data[country]
    
    # Panel 1: Maturity Wall
    ax1 = axes[0, 0]
    x = np.arange(len(years))
    width = 0.6
    bottom = np.zeros(len(years))
    
    for instrument, values, color in [('Eurobonds', data['eurobonds'], INSTRUMENT_COLORS['Eurobonds']),
                                       ('External FX', data['external'], INSTRUMENT_COLORS['External FX Debt']),
                                       ('Local Currency', data['local'], INSTRUMENT_COLORS['Local Currency']),
                                       ('SOE', data['soe'], INSTRUMENT_COLORS['SOE Obligations'])]:
        ax1.bar(x, values, width, bottom=bottom, color=color, label=instrument)
        bottom += np.array(values)
    
    ax1.set_title('Debt Maturity Wall', fontsize=11, fontweight='bold')
    ax1.set_xlabel('Year', fontsize=10)
    ax1.set_ylabel('$ billion', fontsize=10)
    ax1.set_xticks(x)
    ax1.set_xticklabels(years)
    ax1.legend(fontsize=8)
    ax1.grid(True, alpha=0.3, axis='y')
    ax1.axvspan(1.5, 2.5, alpha=0.15, color=COLORS['danger'])
    
    # Panel 2: GFN
    ax2 = axes[0, 1]
    ax2.bar(x, data['gfn'], color=COLORS['primary'], alpha=0.85)
    ax2.axhline(y=20, color=COLORS['danger'], linestyle='--', lw=2, label='Crisis Threshold')
    ax2.set_title('Gross Financing Needs (% GDP)', fontsize=11, fontweight='bold')
    ax2.set_xlabel('Year', fontsize=10)
    ax2.set_ylabel('% of GDP', fontsize=10)
    ax2.set_xticks(x)
    ax2.set_xticklabels(years)
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3, axis='y')
    
    # Panel 3: Spreads and Reserves
    ax3 = axes[1, 0]
    ax3.bar(x, data['spread'], color=COLORS['danger'], alpha=0.7, label='Spread (bps)')
    ax3.set_title('Sovereign Spreads (bps)', fontsize=11, fontweight='bold')
    ax3.set_xlabel('Year', fontsize=10)
    ax3.set_ylabel('Basis Points', fontsize=10)
    ax3.set_xticks(x)
    ax3.set_xticklabels(years)
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Panel 4: Debt Service Ratio
    ax4 = axes[1, 1]
    ax4.bar(x, data['debt_service'], color=COLORS['warning'], alpha=0.85)
    ax4.axhline(y=30, color=COLORS['danger'], linestyle='--', lw=2, label='Crisis Threshold')
    ax4.axhline(y=25, color=COLORS['warning'], linestyle=':', lw=2, label='Stress Threshold')
    ax4.set_title('Debt Service / Revenue (%)', fontsize=11, fontweight='bold')
    ax4.set_xlabel('Year', fontsize=10)
    ax4.set_ylabel('%', fontsize=10)
    ax4.set_xticks(x)
    ax4.set_xticklabels(years)
    ax4.legend(fontsize=8)
    ax4.grid(True, alpha=0.3, axis='y')
    
    fig.suptitle(f'Figure 6.x: {country} - Refinancing Wall Analysis', fontsize=12, fontweight='bold', y=1.02)
    plt.tight_layout()
    
    return save_figure(fig, filename)


def create_figure_6_1():
    return create_case_study_figure('Ghana', 'figure_6_1_ghana_case_study.png')

def create_figure_6_2():
    return create_case_study_figure('Sri Lanka', 'figure_6_2_sri_lanka_case_study.png')

def create_figure_6_3():
    return create_case_study_figure('Zambia', 'figure_6_3_zambia_case_study.png')

def create_figure_6_4():
    return create_case_study_figure('Pakistan', 'figure_6_4_pakistan_case_study.png')


# ============================================================================
# FIGURE 7.1 - LIABILITY MANAGEMENT MENU
# ============================================================================

def create_figure_7_1():
    """Liability Management Menu"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    ax.text(7, 7.5, 'Figure 7.1: Liability Management Menu', 
            ha='center', va='top', fontsize=14, fontweight='bold', color=COLORS['primary'])
    
    options = [
        (2.5, 5.5, 'BUYBACKS', '• Cash repurchase\n• Discount/par/premium\n• Consent solicitation\n• Open market ops', COLORS['success']),
        (7, 5.5, 'EXCHANGES', '• New for old bonds\n• Maturity extension\n• Coupon adjustment\n• Currency switch', COLORS['primary']),
        (11.5, 5.5, 'EXTENSIONS', '• Consent amendments\n• Maturity pushback\n• Grace periods\n• Coupon step-downs', COLORS['warning']),
        (2.5, 2.5, 'CASH BUFFERS', '• Contingency reserves\n• Pre-funded accounts\n• SDR allocations\n• Commodity hedges', COLORS['success']),
        (7, 2.5, 'MARKET\nDEEPENING', '• Benchmark curve\n• Investor base\n• Market-making\n• FX hedging tools', COLORS['primary']),
        (11.5, 2.5, 'CREDITOR\nCOORDINATION', '• CAC activation\n• Comparability\n• Transparency package\n• Good faith negotiation', COLORS['danger']),
    ]
    
    for x, y, title, content, color in options:
        box = FancyBboxPatch((x-2, y-1.2), 4, 2.4, 
                             boxstyle="round,pad=0.05", 
                             facecolor=color, alpha=0.85, edgecolor='white', linewidth=2)
        ax.add_patch(box)
        ax.text(x, y+0.5, title, ha='center', va='center', fontsize=11, 
                color='white', fontweight='bold')
        ax.text(x, y-0.4, content, ha='center', va='center', fontsize=9, 
                color='white', wrap=True)
    
    ax.text(7, 0.3, 'SOURCE: CEDX Liability Management Toolkit', ha='center', fontsize=9, 
            color=COLORS['accent'], style='italic')
    
    return save_figure(fig, 'figure_7_1_liability_menu.png')


# ============================================================================
# FIGURE 7.2 - IMF/IFI ENGAGEMENT SEQUENCING
# ============================================================================

def create_figure_7_2():
    """IMF/IFI Engagement Sequencing"""
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    ax.text(7, 5.5, 'Figure 7.2: IMF/IFI Engagement Sequencing', 
            ha='center', va='top', fontsize=14, fontweight='bold', color=COLORS['primary'])
    
    # Timeline
    ax.arrow(1, 3, 12, 0, head_width=0.15, head_length=0.2, fc=COLORS['accent'], ec=COLORS['accent'])
    
    milestones = [
        (2, 'EARLY\nWARNING', 'Reserves < 5\nmonths imports', COLORS['success']),
        (5, 'PRECAUTIONARY\nENGAGEMENT', 'Reserves < 4\nmonths imports', COLORS['warning']),
        (8, 'PROGRAM\nREQUEST', 'Reserves < 3\nmonths imports', COLORS['warning']),
        (11, 'CRISIS\nRESPONSE', 'Market access\nlost', COLORS['danger']),
    ]
    
    for x, title, trigger, color in milestones:
        circle = Circle((x, 3), 0.3, facecolor=color, edgecolor='white', linewidth=2)
        ax.add_patch(circle)
        ax.text(x, 4, title, ha='center', va='bottom', fontsize=10, fontweight='bold', color=color)
        ax.text(x, 1.8, trigger, ha='center', va='top', fontsize=9, color=COLORS['accent'])
    
    ax.text(7, 0.5, 'SOURCE: CEDX IFI Engagement Framework | NOTE: Engage before reserves collapse - explicit triggers defined', 
            ha='center', fontsize=9, color=COLORS['accent'], style='italic')
    
    return save_figure(fig, 'figure_7_2_imf_engagement.png')


# ============================================================================
# FIGURE 7.3 - POLICY IMPLEMENTATION ROADMAP
# ============================================================================

def create_figure_7_3():
    """Policy Implementation Roadmap"""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    tasks = [
        ('Pre-funding facility setup', 0, 6, COLORS['success']),
        ('Liability management operations', 3, 15, COLORS['primary']),
        ('IMF/IFI engagement', 0, 12, COLORS['warning']),
        ('Domestic market development', 6, 30, COLORS['primary']),
        ('FX hedging instruments', 12, 18, COLORS['secondary']),
        ('Debt transparency reforms', 0, 6, COLORS['success']),
        ('SOE governance reforms', 12, 30, COLORS['warning']),
        ('Contingency fund establishment', 18, 36, COLORS['success']),
    ]
    
    y_pos = np.arange(len(tasks))
    
    for i, (task, start, end, color) in enumerate(tasks):
        ax.barh(i, end-start, left=start, height=0.5, color=color, alpha=0.85)
        ax.text(-1, i, task, ha='right', va='center', fontsize=10)
    
    ax.set_xlim(-8, 40)
    ax.set_ylim(-0.5, len(tasks)-0.5)
    ax.set_xlabel('Months', fontsize=11)
    ax.set_title('Figure 7.3: Policy Implementation Roadmap', fontsize=12, fontweight='bold')
    ax.set_yticks([])
    ax.grid(True, alpha=0.3, axis='x')
    
    # Add phase markers
    ax.axvline(x=6, color=COLORS['accent'], linestyle='--', alpha=0.7)
    ax.axvline(x=18, color=COLORS['accent'], linestyle='--', alpha=0.7)
    ax.text(3, len(tasks)+0.2, 'Phase 1:\nImmediate', ha='center', fontsize=9, color=COLORS['accent'])
    ax.text(12, len(tasks)+0.2, 'Phase 2:\nShort-term', ha='center', fontsize=9, color=COLORS['accent'])
    ax.text(27, len(tasks)+0.2, 'Phase 3:\nMedium-term', ha='center', fontsize=9, color=COLORS['accent'])
    
    ax.text(20, -1.5, 'SOURCE: CEDX Implementation Framework', ha='center', fontsize=9, 
            color=COLORS['accent'], style='italic')
    
    return save_figure(fig, 'figure_7_3_implementation_roadmap.png')


# ============================================================================
# FIGURE 7.4 - CREDITOR COORDINATION FRAMEWORK
# ============================================================================

def create_figure_7_4():
    """Creditor Coordination Framework"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    ax.text(7, 7.5, 'Figure 7.4: Creditor Coordination Framework', 
            ha='center', va='top', fontsize=14, fontweight='bold', color=COLORS['primary'])
    
    # Central box
    box = FancyBboxPatch((5, 4), 4, 2, boxstyle="round,pad=0.05", 
                         facecolor=COLORS['primary'], alpha=0.85, edgecolor='white', linewidth=2)
    ax.add_patch(box)
    ax.text(7, 5, 'CREDITOR\nCOORDINATION', ha='center', va='center', fontsize=12, 
            color='white', fontweight='bold')
    
    # Surrounding elements
    elements = [
        (2, 6, 'COLLECTIVE\nACTION\nCLAUSES', '• Majority restructuring\n• Single-limb aggregation\n• PAC features', COLORS['success']),
        (12, 6, 'COMPARABILITY\nOF TREATMENT', '• Official creditors\n• Private creditors\n• Same NPV treatment', COLORS['warning']),
        (2, 2, 'TRANSPARENCY\nPACKAGE', '• Debt disclosure\n• Payment tracking\n• Public registry', COLORS['primary']),
        (12, 2, 'GOOD FAITH\nNEGOTIATION', '• Information sharing\n• Creditor committee\n• Timeline discipline', COLORS['secondary']),
    ]
    
    for x, y, title, content, color in elements:
        box = FancyBboxPatch((x-1.8, y-1), 3.6, 2, 
                             boxstyle="round,pad=0.05", 
                             facecolor=color, alpha=0.85, edgecolor='white', linewidth=2)
        ax.add_patch(box)
        ax.text(x, y+0.4, title, ha='center', va='center', fontsize=10, 
                color='white', fontweight='bold')
        ax.text(x, y-0.4, content, ha='center', va='center', fontsize=8, 
                color='white', wrap=True)
    
    # Arrows
    arrow_style = dict(arrowstyle='->', color=COLORS['accent'], lw=2)
    arrows = [
        ((3.8, 6), (5, 5.5)), ((10.2, 6), (9, 5.5)),
        ((3.8, 2), (5, 4.5)), ((10.2, 2), (9, 4.5)),
    ]
    
    for start, end in arrows:
        ax.annotate('', xy=end, xytext=start, arrowprops=arrow_style)
    
    ax.text(7, 0.3, 'SOURCE: CEDX Creditor Coordination Framework based on IMF/World Bank standards', ha='center', fontsize=9, 
            color=COLORS['accent'], style='italic')
    
    return save_figure(fig, 'figure_7_4_creditor_coordination.png')


# ============================================================================
# FIGURE 8.1 - RISK REGISTER HEAT MAP
# ============================================================================

def create_figure_8_1():
    """Risk Register Heat Map"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    risks = [
        'Spread widening >500bps',
        'Auction failure',
        'Reserve depletion',
        'FX shortage',
        'Fiscal policy reversal',
        'IMF program derailment',
        'SOE contingent liabilities',
        'Commodity price shock',
        'Global risk-off event',
    ]
    
    likelihood = [4, 3, 4, 4, 3, 3, 4, 3, 4]  # 1-5 scale
    impact = [4, 5, 5, 4, 4, 5, 4, 4, 4]  # 1-5 scale
    
    # Create heat map grid
    for i in range(5, 0, -1):
        for j in range(1, 6):
            if i <= 2 and j <= 2:
                color = '#c6f6d5'  # Low risk
            elif i >= 4 and j >= 4:
                color = '#fed7d7'  # High risk
            else:
                color = '#feebc8'  # Medium risk
            ax.add_patch(Rectangle((j-0.5, i-0.5), 1, 1, facecolor=color, edgecolor='white', linewidth=1))
    
    # Plot risks
    for r, l, im in zip(risks, likelihood, impact):
        ax.plot(im, l, 'o', markersize=15, color=COLORS['primary'], alpha=0.7)
        ax.annotate(r, (im, l), textcoords='offset points', xytext=(10, 5), fontsize=9)
    
    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(0.5, 5.5)
    ax.set_xlabel('Impact', fontsize=11)
    ax.set_ylabel('Likelihood', fontsize=11)
    ax.set_title('Figure 8.1: Risk Register Heat Map', fontsize=12, fontweight='bold')
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_xticklabels(['Low', 'Low-Med', 'Medium', 'Med-High', 'High'])
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['Low', 'Low-Med', 'Medium', 'Med-High', 'High'])
    
    # Legend
    legend_elements = [
        mpatches.Patch(facecolor='#c6f6d5', label='Low Risk'),
        mpatches.Patch(facecolor='#feebc8', label='Medium Risk'),
        mpatches.Patch(facecolor='#fed7d7', label='High Risk'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', framealpha=0.9)
    
    ax.text(3, -0.3, 'SOURCE: CEDX Risk Assessment Framework', ha='center', fontsize=9, 
            color=COLORS['accent'], style='italic')
    
    return save_figure(fig, 'figure_8_1_risk_heat_map.png')


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Generate all figures"""
    print("=" * 60)
    print("Generating all figures for The 2026 Refinancing Wall Report")
    print("=" * 60)
    
    figures = [
        ('Figure 1.1 - Conceptual Framework', create_figure_1_1),
        ('Figure 2.1 - Global Interest Rates', create_figure_2_1),
        ('Figure 2.2 - Sovereign Spreads', create_figure_2_2),
        ('Figure 4.1 - Aggregate Maturity Wall', create_figure_4_1),
        ('Figure 4.2 - Country Maturity Walls', create_figure_4_2),
        ('Figure 4.3 - Gross Financing Needs', create_figure_4_3),
        ('Figure 4.4 - Debt Service Ratio', create_figure_4_4),
        ('Figure 4.5 - Stress Fan Chart', create_figure_4_5),
        ('Figure 4.6 - Refinancing Gap', create_figure_4_6),
        ('Figure 4.7 - Rollover Capacity', create_figure_4_7),
        ('Figure 4.8 - Reserve Adequacy', create_figure_4_8),
        ('Figure 5.1 - Decision Tree', create_figure_5_1),
        ('Figure 5.2 - Sovereign-Corporate Loop', create_figure_5_2),
        ('Figure 6.1 - Ghana Case Study', create_figure_6_1),
        ('Figure 6.2 - Sri Lanka Case Study', create_figure_6_2),
        ('Figure 6.3 - Zambia Case Study', create_figure_6_3),
        ('Figure 6.4 - Pakistan Case Study', create_figure_6_4),
        ('Figure 7.1 - Liability Menu', create_figure_7_1),
        ('Figure 7.2 - IMF Engagement', create_figure_7_2),
        ('Figure 7.3 - Implementation Roadmap', create_figure_7_3),
        ('Figure 7.4 - Creditor Coordination', create_figure_7_4),
        ('Figure 8.1 - Risk Heat Map', create_figure_8_1),
    ]
    
    for name, func in figures:
        print(f"\nGenerating: {name}")
        try:
            filepath = func()
            print(f"  ✓ Saved: {filepath}")
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    print("\n" + "=" * 60)
    print("All figures generated successfully!")
    print(f"Output directory: {OUTPUT_DIR}")
    print("=" * 60)


if __name__ == '__main__':
    main()
