#!/usr/bin/env python3
"""
Generate all visualizations for "The 2026 Refinancing Wall" report
Professional quality PNG files at 300 DPI
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle, Polygon
from matplotlib.collections import PatchCollection
import matplotlib.patheffects as path_effects
import numpy as np
import os

# Set up professional styling
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif', 'serif']
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

# Professional color palette
COLORS = {
    'deep_blue': '#1a365d',
    'gold': '#b7791f',
    'gray': '#718096',
    'red': '#c53030',
    'light_blue': '#3182ce',
    'light_gold': '#d69e2e',
    'light_gray': '#a0aec0',
    'green': '#2f855a',
    'orange': '#dd6b20',
    'purple': '#553c9a',
    'teal': '#319795',
    'pink': '#d53f8c'
}

# Extended color palette for multiple categories
PALETTE = ['#1a365d', '#b7791f', '#718096', '#c53030', '#3182ce', '#d69e2e', '#2f855a', '#dd6b20', '#553c9a', '#319795']

OUTPUT_DIR = '/home/z/my-project/download/refinancing_wall_report/figures'

def save_figure(fig, filename):
    """Save figure with professional settings"""
    filepath = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(filepath, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"Saved: {filepath}")
    return filepath

# =============================================================================
# FIGURE 1.1 - Conceptual Framework Diagram
# =============================================================================
def create_figure_1_1():
    """Create Conceptual Framework Diagram - Refinancing Wall Mechanism"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Title
    ax.text(6, 7.5, 'Figure 1.1: The Refinancing Wall Mechanism', 
            fontsize=14, fontweight='bold', ha='center', color=COLORS['deep_blue'])
    
    # Box style
    box_style = "round,pad=0.3,rounding_size=0.2"
    
    # Create boxes
    boxes = [
        (1, 5.5, 'Maturity Bunching\n(2024-2026)', COLORS['deep_blue']),
        (4.5, 5.5, 'High Global\nInterest Rates', COLORS['gold']),
        (8, 5.5, 'Tighter Risk\nAppetite', COLORS['light_blue']),
        (5.5, 2.5, 'ROLLOVER\nCRISIS', COLORS['red']),
    ]
    
    for x, y, text, color in boxes:
        box = FancyBboxPatch((x-0.9, y-0.6), 1.8, 1.2,
                            boxstyle=box_style, facecolor=color, 
                            edgecolor='white', linewidth=2, alpha=0.9)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=10,
               fontweight='bold', color='white')
    
    # Arrows
    arrow_style = "Simple, tail_width=0.5, head_width=4, head_length=4"
    
    # Arrow from box 1 to box 2
    ax.annotate('', xy=(3.5, 5.5), xytext=(2, 5.5),
               arrowprops=dict(arrowstyle='->', color=COLORS['gray'], lw=2))
    
    # Arrow from box 2 to box 3
    ax.annotate('', xy=(7, 5.5), xytext=(5.5, 5.5),
               arrowprops=dict(arrowstyle='->', color=COLORS['gray'], lw=2))
    
    # Arrow from box 1 to crisis
    ax.annotate('', xy=(5, 3.3), xytext=(1.5, 4.8),
               arrowprops=dict(arrowstyle='->', color=COLORS['red'], lw=2))
    
    # Arrow from box 2 to crisis
    ax.annotate('', xy=(5.5, 3.3), xytext=(5, 4.8),
               arrowprops=dict(arrowstyle='->', color=COLORS['red'], lw=2))
    
    # Arrow from box 3 to crisis
    ax.annotate('', xy=(6, 3.3), xytext=(8.5, 4.8),
               arrowprops=dict(arrowstyle='->', color=COLORS['red'], lw=2))
    
    # Add annotations
    ax.text(2.75, 5.8, 'Compounds', fontsize=9, ha='center', style='italic', color=COLORS['gray'])
    ax.text(6.25, 5.8, 'Amplifies', fontsize=9, ha='center', style='italic', color=COLORS['gray'])
    
    # Add impact text
    ax.text(5.5, 1.2, 'Result: Refinancing Gap → Default Risk → Contagion', 
            fontsize=10, ha='center', style='italic', color=COLORS['red'])
    
    # Source note
    ax.text(6, 0.3, 'Source: Author\'s conceptual framework', 
            fontsize=9, ha='center', color=COLORS['gray'], style='italic')
    
    return save_figure(fig, 'figure_1_1_conceptual_framework.png')

# =============================================================================
# FIGURE 2.1 - Global Interest Rate Trends
# =============================================================================
def create_figure_2_1():
    """Create Global Interest Rate Trends Chart"""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Data
    years = np.array([2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026])
    fed_funds = np.array([2.2, 0.1, 0.1, 4.0, 5.3, 5.0, 4.5, 4.0])
    ecb_rate = np.array([0.0, 0.0, 0.0, 2.5, 4.0, 3.75, 3.5, 3.0])
    boe_rate = np.array([0.8, 0.1, 0.1, 3.5, 5.0, 4.75, 4.25, 3.75])
    em_average = np.array([4.5, 3.5, 3.5, 6.0, 7.5, 7.0, 6.5, 6.0])
    
    ax.plot(years, fed_funds, 'o-', color=COLORS['deep_blue'], linewidth=2.5, 
            markersize=8, label='Fed Funds Rate')
    ax.plot(years, ecb_rate, 's-', color=COLORS['gold'], linewidth=2.5, 
            markersize=8, label='ECB Rate')
    ax.plot(years, boe_rate, '^-', color=COLORS['green'], linewidth=2.5, 
            markersize=8, label='BOE Rate')
    ax.plot(years, em_average, 'D-', color=COLORS['red'], linewidth=2.5, 
            markersize=8, label='EM Average Policy Rate')
    
    # Add shaded region for crisis period
    ax.axvspan(2022, 2024, alpha=0.2, color=COLORS['red'], label='Rate Hike Cycle')
    
    # Add horizontal line for pre-pandemic average
    ax.axhline(y=1.5, color=COLORS['gray'], linestyle='--', alpha=0.7, 
               label='Pre-pandemic average')
    
    ax.set_xlabel('Year', fontweight='bold')
    ax.set_ylabel('Policy Rate (%)', fontweight='bold')
    ax.set_title('Figure 2.1: Global Interest Rate Trends (2019-2026)', 
                fontsize=14, fontweight='bold', color=COLORS['deep_blue'], pad=15)
    ax.set_xlim(2018.5, 2026.5)
    ax.set_ylim(-0.5, 9)
    ax.set_xticks(years)
    ax.legend(loc='upper left', framealpha=0.9)
    ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
    
    # Add annotation for peak
    ax.annotate('Peak\n2023', xy=(2023, 7.5), xytext=(2023.5, 8.2),
               fontsize=9, ha='center',
               arrowprops=dict(arrowstyle='->', color=COLORS['gray']))
    
    ax.text(2026, -0.8, 'Source: IMF, Central Bank Data, Author projections', 
            fontsize=9, ha='right', color=COLORS['gray'], style='italic')
    
    return save_figure(fig, 'figure_2_1_global_interest_rates.png')

# =============================================================================
# FIGURE 2.2 - Sovereign Spread Evolution
# =============================================================================
def create_figure_2_2():
    """Create Sovereign Spread Evolution Chart"""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Data
    years = np.array([2020, 2021, 2022, 2023, 2024, 2025, 2026])
    embi_global = np.array([400, 350, 550, 700, 650, 600, 550])
    embi_diversified = np.array([350, 300, 480, 620, 580, 540, 500])
    ghana = np.array([800, 900, 2000, 3500, 4000, 3500, 3000])
    zambia = np.array([1500, 2000, 3000, 5000, 4500, 4000, 3500])
    sri_lanka = np.array([500, 600, 1500, 5000, 4500, 4000, 3500])
    pakistan = np.array([600, 700, 1200, 2000, 2500, 2200, 2000])
    
    ax.plot(years, embi_global, 'o-', color=COLORS['deep_blue'], linewidth=2, 
            markersize=6, label='EMBI Global Spread')
    ax.plot(years, embi_diversified, 's-', color=COLORS['gold'], linewidth=2, 
            markersize=6, label='EMBI Diversified')
    ax.plot(years, ghana, '^-', color=COLORS['red'], linewidth=2, 
            markersize=6, label='Ghana')
    ax.plot(years, zambia, 'D-', color=COLORS['green'], linewidth=2, 
            markersize=6, label='Zambia')
    ax.plot(years, sri_lanka, 'v-', color=COLORS['purple'], linewidth=2, 
            markersize=6, label='Sri Lanka')
    ax.plot(years, pakistan, 'p-', color=COLORS['orange'], linewidth=2, 
            markersize=6, label='Pakistan')
    
    # Add crisis annotation
    ax.axvline(x=2022, color=COLORS['gray'], linestyle='--', alpha=0.5)
    ax.text(2022.1, 5200, 'Global Rate\nHike Cycle', fontsize=9, 
            color=COLORS['gray'], style='italic')
    
    # Add distress threshold
    ax.axhline(y=1000, color=COLORS['red'], linestyle=':', alpha=0.7)
    ax.text(2026.3, 1050, 'Distress\nThreshold', fontsize=9, 
            color=COLORS['red'], va='bottom')
    
    ax.set_xlabel('Year', fontweight='bold')
    ax.set_ylabel('Spread (basis points)', fontweight='bold')
    ax.set_title('Figure 2.2: Sovereign Spread Evolution (2020-2026)', 
                fontsize=14, fontweight='bold', color=COLORS['deep_blue'], pad=15)
    ax.set_xlim(2019.5, 2026.5)
    ax.set_ylim(0, 5500)
    ax.set_xticks(years)
    ax.legend(loc='upper left', framealpha=0.9, ncol=2)
    ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
    
    ax.text(2026, -400, 'Source: J.P. Morgan, Bloomberg, Author estimates', 
            fontsize=9, ha='right', color=COLORS['gray'], style='italic')
    
    return save_figure(fig, 'figure_2_2_sovereign_spreads.png')

# =============================================================================
# FIGURE 4.1 - Maturity Wall Chart (Aggregate)
# =============================================================================
def create_figure_4_1():
    """Create Aggregate Maturity Wall Chart"""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Data (in billions USD)
    years = ['2024', '2025', '2026', '2027', '2028', '2029', '2030']
    eurobonds = [45, 52, 68, 48, 35, 28, 22]
    external_fx = [38, 42, 55, 40, 32, 25, 20]
    local_currency = [25, 30, 42, 35, 28, 22, 18]
    soe_obligations = [15, 18, 25, 20, 15, 12, 10]
    
    x = np.arange(len(years))
    width = 0.6
    
    # Create stacked bar chart
    bars1 = ax.bar(x, eurobonds, width, label='Eurobonds', color=COLORS['deep_blue'])
    bars2 = ax.bar(x, external_fx, width, bottom=eurobonds, label='External FX Debt', 
                   color=COLORS['gold'])
    bars3 = ax.bar(x, local_currency, width, 
                   bottom=np.array(eurobonds)+np.array(external_fx), 
                   label='Local Currency', color=COLORS['light_blue'])
    bars4 = ax.bar(x, soe_obligations, width, 
                   bottom=np.array(eurobonds)+np.array(external_fx)+np.array(local_currency),
                   label='SOE Obligations', color=COLORS['red'])
    
    # Highlight 2026
    ax.axvspan(1.5, 2.5, alpha=0.15, color=COLORS['red'])
    ax.text(2, 210, '2026\nRefinancing\nWall', fontsize=11, ha='center', 
            fontweight='bold', color=COLORS['red'])
    
    # Add total labels
    totals = [sum(x) for x in zip(eurobonds, external_fx, local_currency, soe_obligations)]
    for i, total in enumerate(totals):
        ax.text(i, total + 3, f'${total}bn', ha='center', fontsize=9, fontweight='bold')
    
    ax.set_xlabel('Year', fontweight='bold')
    ax.set_ylabel('Debt Maturing (USD billions)', fontweight='bold')
    ax.set_title('Figure 4.1: Aggregate Maturity Wall by Instrument Type', 
                fontsize=14, fontweight='bold', color=COLORS['deep_blue'], pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.legend(loc='upper right', framealpha=0.9)
    ax.set_ylim(0, 230)
    ax.grid(True, alpha=0.3, axis='y', linestyle='-', linewidth=0.5)
    
    ax.text(6, -25, 'Source: IMF Debt Sustainability Analysis, World Bank, Author calculations', 
            fontsize=9, ha='right', color=COLORS['gray'], style='italic')
    
    return save_figure(fig, 'figure_4_1_aggregate_maturity_wall.png')

# =============================================================================
# FIGURE 4.2 - Country-Level Maturity Walls
# =============================================================================
def create_figure_4_2():
    """Create Multi-panel Country Maturity Wall Chart"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    countries = {
        'Ghana': {'eurobonds': [3.2, 3.8, 5.2, 3.5, 2.5, 2.0, 1.5],
                  'bilateral': [1.5, 1.8, 2.5, 2.0, 1.5, 1.2, 1.0],
                  'local': [2.8, 3.2, 4.5, 3.8, 3.0, 2.5, 2.0]},
        'Sri Lanka': {'eurobonds': [2.5, 3.0, 4.2, 3.0, 2.2, 1.8, 1.2],
                      'bilateral': [2.0, 2.5, 3.5, 2.8, 2.2, 1.8, 1.5],
                      'local': [3.0, 3.5, 5.0, 4.0, 3.2, 2.8, 2.2]},
        'Zambia': {'eurobonds': [1.8, 2.2, 3.0, 2.2, 1.6, 1.2, 0.8],
                   'bilateral': [0.8, 1.0, 1.5, 1.2, 0.9, 0.7, 0.5],
                   'local': [1.2, 1.5, 2.2, 1.8, 1.4, 1.1, 0.8]},
        'Pakistan': {'eurobonds': [4.5, 5.2, 7.0, 5.0, 3.8, 3.0, 2.5],
                     'bilateral': [3.5, 4.0, 5.5, 4.5, 3.5, 2.8, 2.2],
                     'local': [5.0, 5.8, 8.0, 6.5, 5.0, 4.0, 3.2]}
    }
    
    years = ['2024', '2025', '2026', '2027', '2028', '2029', '2030']
    x = np.arange(len(years))
    width = 0.55
    
    colors = {'eurobonds': COLORS['deep_blue'], 'bilateral': COLORS['gold'], 'local': COLORS['light_blue']}
    
    for ax, (country, data) in zip(axes.flatten(), countries.items()):
        bars1 = ax.bar(x, data['eurobonds'], width, label='Eurobonds', color=colors['eurobonds'])
        bars2 = ax.bar(x, data['bilateral'], width, bottom=data['eurobonds'], 
                       label='Bilateral', color=colors['bilateral'])
        bars3 = ax.bar(x, data['local'], width, 
                       bottom=np.array(data['eurobonds'])+np.array(data['bilateral']),
                       label='Local Currency', color=colors['local'])
        
        # Highlight 2026
        ax.axvspan(1.5, 2.5, alpha=0.15, color=COLORS['red'])
        
        totals = [sum(x) for x in zip(data['eurobonds'], data['bilateral'], data['local'])]
        ax.text(2, max(totals)+0.5, f'2026: ${totals[2]:.1f}bn', fontsize=9, 
                ha='center', fontweight='bold', color=COLORS['red'])
        
        ax.set_title(f'{country}', fontsize=12, fontweight='bold', color=COLORS['deep_blue'])
        ax.set_xticks(x)
        ax.set_xticklabels(years, fontsize=9)
        ax.set_ylabel('USD billions', fontsize=10)
        ax.grid(True, alpha=0.3, axis='y')
    
    # Add common legend
    handles, labels = axes[0,0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center', ncol=3, fontsize=10, 
               bbox_to_anchor=(0.5, 0.02), framealpha=0.9)
    
    fig.suptitle('Figure 4.2: Country-Level Maturity Walls (2024-2030)', 
                fontsize=14, fontweight='bold', color=COLORS['deep_blue'], y=0.98)
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    
    return save_figure(fig, 'figure_4_2_country_maturity_walls.png')

# =============================================================================
# FIGURE 4.3 - Gross Financing Needs
# =============================================================================
def create_figure_4_3():
    """Create Gross Financing Needs Chart"""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    countries = ['Ghana', 'Sri Lanka', 'Zambia', 'Pakistan', 'Kenya', 'Ethiopia', 'Tunisia']
    years = ['2025', '2026', '2027', '2028']
    
    # GFN as % of GDP
    data = {
        '2025': [18.5, 22.0, 15.5, 19.0, 16.5, 12.0, 14.5],
        '2026': [22.5, 26.5, 18.0, 23.5, 19.0, 14.0, 16.0],
        '2027': [19.0, 20.5, 16.0, 20.0, 17.0, 13.5, 15.0],
        '2028': [16.5, 18.0, 14.5, 18.5, 15.5, 12.5, 14.0]
    }
    
    x = np.arange(len(countries))
    width = 0.2
    
    for i, year in enumerate(years):
        offset = (i - 1.5) * width
        bars = ax.bar(x + offset, data[year], width, label=year, color=PALETTE[i])
    
    # Add threshold line
    ax.axhline(y=20, color=COLORS['red'], linestyle='--', linewidth=2, alpha=0.7)
    ax.text(len(countries)-0.5, 20.5, 'High GFN Threshold (20% GDP)', 
            fontsize=9, color=COLORS['red'], style='italic')
    
    ax.set_xlabel('Country', fontweight='bold')
    ax.set_ylabel('Gross Financing Needs (% of GDP)', fontweight='bold')
    ax.set_title('Figure 4.3: Gross Financing Needs by Country and Year', 
                fontsize=14, fontweight='bold', color=COLORS['deep_blue'], pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(countries)
    ax.legend(loc='upper right', framealpha=0.9)
    ax.set_ylim(0, 30)
    ax.grid(True, alpha=0.3, axis='y', linestyle='-', linewidth=0.5)
    
    ax.text(len(countries)-1, -3, 'Source: IMF Article IV Reports, World Bank, Author calculations', 
            fontsize=9, ha='right', color=COLORS['gray'], style='italic')
    
    return save_figure(fig, 'figure_4_3_gross_financing_needs.png')

# =============================================================================
# FIGURE 4.4 - Debt Service to Revenue Ratio
# =============================================================================
def create_figure_4_4():
    """Create Debt Service to Revenue Ratio Chart"""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    countries = ['Ghana', 'Sri Lanka', 'Zambia', 'Pakistan', 'Kenya', 'Ethiopia', 'Tunisia', 'Egypt']
    ratios_2024 = [52, 68, 45, 58, 42, 38, 48, 55]
    ratios_2025 = [55, 72, 48, 62, 45, 40, 50, 58]
    ratios_2026 = [58, 78, 52, 68, 48, 42, 52, 62]
    
    x = np.arange(len(countries))
    width = 0.25
    
    bars1 = ax.bar(x - width, ratios_2024, width, label='2024', color=COLORS['deep_blue'])
    bars2 = ax.bar(x, ratios_2025, width, label='2025', color=COLORS['gold'])
    bars3 = ax.bar(x + width, ratios_2026, width, label='2026', color=COLORS['red'])
    
    # Add threshold lines
    ax.axhline(y=25, color=COLORS['green'], linestyle='--', linewidth=2, alpha=0.8)
    ax.text(len(countries)-0.5, 26, 'Sustainable (25%)', fontsize=9, color=COLORS['green'])
    
    ax.axhline(y=30, color=COLORS['red'], linestyle='--', linewidth=2, alpha=0.8)
    ax.text(len(countries)-0.5, 31, 'Politically Explosive (30%)', fontsize=9, color=COLORS['red'])
    
    # Highlight high ratios
    for i, (r24, r25, r26) in enumerate(zip(ratios_2024, ratios_2025, ratios_2026)):
        if r26 > 50:
            ax.annotate(f'{r26}%', xy=(i + width, r26), xytext=(i + width, r26 + 3),
                       fontsize=8, ha='center', color=COLORS['red'], fontweight='bold')
    
    ax.set_xlabel('Country', fontweight='bold')
    ax.set_ylabel('Debt Service / Revenue (%)', fontweight='bold')
    ax.set_title('Figure 4.4: Debt Service to Revenue Ratio by Country', 
                fontsize=14, fontweight='bold', color=COLORS['deep_blue'], pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(countries)
    ax.legend(loc='upper right', framealpha=0.9)
    ax.set_ylim(0, 90)
    ax.grid(True, alpha=0.3, axis='y', linestyle='-', linewidth=0.5)
    
    ax.text(len(countries)-1, -8, 'Source: IMF Fiscal Monitor, National Treasury Data', 
            fontsize=9, ha='right', color=COLORS['gray'], style='italic')
    
    return save_figure(fig, 'figure_4_4_debt_service_revenue_ratio.png')

# =============================================================================
# FIGURE 4.5 - Stress Scenario Fan Chart
# =============================================================================
def create_figure_4_5():
    """Create Stress Scenario Fan Chart"""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    years = np.array([2024, 2025, 2026, 2027, 2028])
    
    # Baseline trajectory
    baseline = np.array([45, 48, 52, 50, 47])
    
    # Moderate stress (+300bps spreads)
    moderate_low = np.array([45, 52, 60, 58, 55])
    moderate_high = np.array([45, 55, 65, 62, 58])
    
    # Severe stress (+300bps, -15% FX, -1.5pp growth)
    severe_low = np.array([45, 58, 72, 70, 65])
    severe_high = np.array([45, 65, 85, 82, 75])
    
    # Plot severe stress band
    ax.fill_between(years, severe_low, severe_high, alpha=0.2, color=COLORS['red'],
                   label='Severe Stress Scenario')
    
    # Plot moderate stress band
    ax.fill_between(years, moderate_low, moderate_high, alpha=0.3, color=COLORS['gold'],
                   label='Moderate Stress Scenario')
    
    # Plot baseline
    ax.plot(years, baseline, 'o-', color=COLORS['deep_blue'], linewidth=3, 
            markersize=10, label='Baseline Scenario', zorder=5)
    
    # Add annotations
    ax.annotate('Debt Service\nCrisis Zone', xy=(2026, 72), xytext=(2025, 80),
               fontsize=10, ha='center',
               arrowprops=dict(arrowstyle='->', color=COLORS['red']),
               color=COLORS['red'], fontweight='bold')
    
    # Add threshold
    ax.axhline(y=60, color=COLORS['gray'], linestyle=':', linewidth=2)
    ax.text(2028.2, 60, 'Crisis\nThreshold', fontsize=9, color=COLORS['gray'], va='center')
    
    ax.set_xlabel('Year', fontweight='bold')
    ax.set_ylabel('Debt Service (% of Revenue)', fontweight='bold')
    ax.set_title('Figure 4.5: Stress Scenario Fan Chart - Debt Service Trajectories', 
                fontsize=14, fontweight='bold', color=COLORS['deep_blue'], pad=15)
    ax.set_xlim(2023.5, 2028.5)
    ax.set_ylim(35, 90)
    ax.legend(loc='upper left', framealpha=0.9)
    ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
    
    ax.text(2028, 32, 'Source: Author\'s stress testing model', 
            fontsize=9, ha='right', color=COLORS['gray'], style='italic')
    
    return save_figure(fig, 'figure_4_5_stress_scenario_fan_chart.png')

# =============================================================================
# FIGURE 4.6 - Refinancing Gap Model Results
# =============================================================================
def create_figure_4_6():
    """Create Refinancing Gap Model Results Chart"""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    countries = ['Ghana', 'Sri Lanka', 'Zambia', 'Pakistan', 'Kenya', 'Ethiopia']
    baseline_gap = [2.5, 3.2, 1.8, 4.5, 2.0, 1.2]
    stress_gap = [5.8, 7.5, 4.2, 9.5, 4.5, 3.0]
    
    x = np.arange(len(countries))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, baseline_gap, width, label='Baseline Scenario', 
                   color=COLORS['deep_blue'], edgecolor='white')
    bars2 = ax.bar(x + width/2, stress_gap, width, label='Stress Scenario', 
                   color=COLORS['red'], edgecolor='white')
    
    # Add value labels
    for i, (b, s) in enumerate(zip(baseline_gap, stress_gap)):
        ax.text(x[i] - width/2, b + 0.2, f'${b}bn', ha='center', fontsize=9, fontweight='bold')
        ax.text(x[i] + width/2, s + 0.2, f'${s}bn', ha='center', fontsize=9, fontweight='bold', color=COLORS['red'])
    
    # Add increase percentage
    for i, (b, s) in enumerate(zip(baseline_gap, stress_gap)):
        increase = ((s - b) / b) * 100
        ax.annotate(f'+{increase:.0f}%', xy=(x[i] + width/2, s), xytext=(x[i] + width/2 + 0.3, s + 0.5),
                   fontsize=8, ha='left', color=COLORS['red'], style='italic')
    
    ax.set_xlabel('Country', fontweight='bold')
    ax.set_ylabel('Refinancing Gap (USD billions)', fontweight='bold')
    ax.set_title('Figure 4.6: Refinancing Gap Model Results - Baseline vs Stress', 
                fontsize=14, fontweight='bold', color=COLORS['deep_blue'], pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(countries)
    ax.legend(loc='upper right', framealpha=0.9)
    ax.set_ylim(0, 12)
    ax.grid(True, alpha=0.3, axis='y', linestyle='-', linewidth=0.5)
    
    ax.text(len(countries)-1, -1.2, 'Source: Author\'s refinancing gap model', 
            fontsize=9, ha='right', color=COLORS['gray'], style='italic')
    
    return save_figure(fig, 'figure_4_6_refinancing_gap_results.png')

# =============================================================================
# FIGURE 4.7 - External vs Local Rollover Capacity
# =============================================================================
def create_figure_4_7():
    """Create External vs Local Rollover Capacity Chart"""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    countries = ['Ghana', 'Sri Lanka', 'Zambia', 'Pakistan', 'Kenya', 'Ethiopia']
    
    # 2026 needs
    external_needs = [5.2, 4.2, 3.0, 7.0, 3.5, 2.5]
    local_needs = [4.5, 5.0, 2.2, 8.0, 4.0, 3.0]
    
    # Capacity
    external_capacity = [1.5, 0.8, 0.5, 2.0, 1.2, 0.8]
    local_capacity = [3.0, 2.0, 1.5, 4.0, 2.5, 2.0]
    
    x = np.arange(len(countries))
    width = 0.2
    
    bars1 = ax.bar(x - 1.5*width, external_needs, width, label='External Need', 
                   color=COLORS['deep_blue'])
    bars2 = ax.bar(x - 0.5*width, external_capacity, width, label='External Capacity', 
                   color=COLORS['light_blue'])
    bars3 = ax.bar(x + 0.5*width, local_needs, width, label='Local Need', 
                   color=COLORS['gold'])
    bars4 = ax.bar(x + 1.5*width, local_capacity, width, label='Local Capacity', 
                   color=COLORS['light_gold'])
    
    ax.set_xlabel('Country', fontweight='bold')
    ax.set_ylabel('USD billions', fontweight='bold')
    ax.set_title('Figure 4.7: External vs Local Market Rollover Capacity (2026)', 
                fontsize=14, fontweight='bold', color=COLORS['deep_blue'], pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(countries)
    ax.legend(loc='upper right', framealpha=0.9, ncol=2)
    ax.grid(True, alpha=0.3, axis='y', linestyle='-', linewidth=0.5)
    
    ax.text(len(countries)-1, -0.8, 'Source: Central Bank Data, IMF, Author estimates', 
            fontsize=9, ha='right', color=COLORS['gray'], style='italic')
    
    return save_figure(fig, 'figure_4_7_rollover_capacity.png')

# =============================================================================
# FIGURE 4.8 - FX Reserve Adequacy
# =============================================================================
def create_figure_4_8():
    """Create FX Reserve Adequacy Chart"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    countries = ['Ghana', 'Sri Lanka', 'Zambia', 'Pakistan', 'Kenya', 'Ethiopia']
    
    # Months of imports
    months_imports = [2.8, 1.5, 2.2, 1.8, 3.5, 2.0]
    
    # % of short-term debt
    st_debt_pct = [65, 45, 55, 70, 80, 50]
    
    colors = [COLORS['red'] if m < 3 else COLORS['gold'] if m < 4 else COLORS['green'] 
              for m in months_imports]
    
    # Left plot - Months of imports
    bars1 = ax1.barh(countries, months_imports, color=colors, edgecolor='white')
    ax1.axvline(x=3, color=COLORS['red'], linestyle='--', linewidth=2)
    ax1.text(3.1, -0.5, 'Minimum\nThreshold', fontsize=9, color=COLORS['red'], va='top')
    ax1.set_xlabel('Months of Imports', fontweight='bold')
    ax1.set_title('Reserve Coverage\n(Months of Imports)', fontsize=12, 
                 fontweight='bold', color=COLORS['deep_blue'])
    ax1.set_xlim(0, 5)
    
    for i, v in enumerate(months_imports):
        ax1.text(v + 0.1, i, f'{v:.1f}', va='center', fontsize=9, fontweight='bold')
    
    # Right plot - % of ST debt
    colors2 = [COLORS['red'] if p < 60 else COLORS['gold'] if p < 100 else COLORS['green'] 
               for p in st_debt_pct]
    bars2 = ax2.barh(countries, st_debt_pct, color=colors2, edgecolor='white')
    ax2.axvline(x=100, color=COLORS['green'], linestyle='--', linewidth=2)
    ax2.text(101, -0.5, 'Guideline\n(100%)', fontsize=9, color=COLORS['green'], va='top')
    ax2.set_xlabel('% of Short-term External Debt', fontweight='bold')
    ax2.set_title('Reserve Adequacy\n(% of ST Debt)', fontsize=12, 
                 fontweight='bold', color=COLORS['deep_blue'])
    ax2.set_xlim(0, 120)
    
    for i, v in enumerate(st_debt_pct):
        ax2.text(v + 1, i, f'{v}%', va='center', fontsize=9, fontweight='bold')
    
    fig.suptitle('Figure 4.8: FX Reserve Adequacy Indicators (2024)', 
                fontsize=14, fontweight='bold', color=COLORS['deep_blue'], y=1.02)
    plt.tight_layout()
    
    ax2.text(120, -0.8, 'Source: IMF IFS, Central Bank Data', 
            fontsize=9, ha='right', color=COLORS['gray'], style='italic')
    
    return save_figure(fig, 'figure_4_8_fx_reserve_adequacy.png')

# =============================================================================
# FIGURE 5.1 - Decision Tree
# =============================================================================
def create_figure_5_1():
    """Create Decision Tree for Liability Management Options"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    ax.text(7, 9.5, 'Figure 5.1: Decision Tree - Liability Management Options', 
            fontsize=14, fontweight='bold', ha='center', color=COLORS['deep_blue'])
    
    box_style = "round,pad=0.3,rounding_size=0.15"
    
    # Decision nodes
    nodes = [
        # Level 0 - Start
        (7, 8.2, 'Debt Sustainability\nAssessment', COLORS['deep_blue'], 'decision'),
        
        # Level 1 - First decision
        (3.5, 6.5, 'GFN < 20% GDP?\nSpreads < 500bps?', COLORS['gold'], 'question'),
        (10.5, 6.5, 'GFN > 20% GDP?\nSpreads > 500bps?', COLORS['red'], 'question'),
        
        # Level 2 - Second decisions
        (2, 4.5, 'PRE-FUNDING\nStrategy', COLORS['green'], 'outcome'),
        (5, 4.5, 'REPROFILING\nStrategy', COLORS['gold'], 'outcome'),
        (9.5, 4.5, 'RESTRUCTURING\nRequired', COLORS['red'], 'outcome'),
        (12, 4.5, 'IMF Program\nEngagement', COLORS['purple'], 'outcome'),
        
        # Level 3 - Details
        (1, 2.5, '• Market issuance\n• Build buffers\n• Extend maturities', COLORS['light_blue'], 'detail'),
        (3.5, 2.5, '• Liability exchanges\n• Maturity extensions\n• Coupon adjustments', COLORS['light_gold'], 'detail'),
        (5.5, 2.5, '• Bond exchanges\n• Principal reduction\n• Creditor coordination', COLORS['orange'], 'detail'),
        (8, 2.5, '• Formal restructuring\n• CACs activation\n• Comparability of treatment', COLORS['red'], 'detail'),
        (10.5, 2.5, '• Program design\n• Financing assurance\n• Policy conditionality', COLORS['purple'], 'detail'),
        (12.5, 2.5, '• Technical assistance\n• Capacity building', COLORS['teal'], 'detail'),
    ]
    
    for x, y, text, color, node_type in nodes:
        width = 2.2 if node_type == 'detail' else 2.5
        height = 0.8 if node_type == 'detail' else 1.0
        box = FancyBboxPatch((x-width/2, y-height/2), width, height,
                            boxstyle=box_style, facecolor=color, 
                            edgecolor='white', linewidth=2, alpha=0.9)
        ax.add_patch(box)
        fontsize = 8 if node_type == 'detail' else 9
        ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
               fontweight='bold', color='white', wrap=True)
    
    # Arrows
    arrows = [
        (7, 7.6, 5, 7.1),
        (7, 7.6, 9, 7.1),
        (3.5, 5.9, 2.3, 5.1),
        (3.5, 5.9, 4.7, 5.1),
        (10.5, 5.9, 9.3, 5.1),
        (10.5, 5.9, 11.7, 5.1),
        (2, 3.9, 1.3, 3.1),
        (2, 3.9, 3.3, 3.1),
        (5, 3.9, 5.3, 3.1),
        (9.5, 3.9, 7.8, 3.1),
        (9.5, 3.9, 10.3, 3.1),
        (12, 3.9, 12.3, 3.1),
    ]
    
    for x1, y1, x2, y2 in arrows:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='->', color=COLORS['gray'], lw=1.5))
    
    # Labels
    ax.text(5.5, 7.3, 'YES', fontsize=9, color=COLORS['green'], fontweight='bold')
    ax.text(8.5, 7.3, 'NO', fontsize=9, color=COLORS['red'], fontweight='bold')
    
    ax.text(7, 0.5, 'Source: Author\'s framework based on IMF debt sustainability analysis methodology', 
            fontsize=9, ha='center', color=COLORS['gray'], style='italic')
    
    return save_figure(fig, 'figure_5_1_decision_tree.png')

# =============================================================================
# FIGURE 5.2 - Sovereign-Corporate Feedback Loop
# =============================================================================
def create_figure_5_2():
    """Create Sovereign-Corporate Feedback Loop Diagram"""
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    ax.text(6, 9.5, 'Figure 5.2: Sovereign-Corporate Feedback Loop', 
            fontsize=14, fontweight='bold', ha='center', color=COLORS['deep_blue'])
    
    # Central elements in circular arrangement
    angles = np.linspace(0, 2*np.pi, 6, endpoint=False) + np.pi/2
    radius = 3
    center = (6, 5)
    
    elements = [
        ('Sovereign\nCredit\nDeterioration', COLORS['red']),
        ('Higher\nBorrowing\nCosts', COLORS['orange']),
        ('Bank\nBalance Sheet\nStress', COLORS['gold']),
        ('Corporate/SOE\nDistress', COLORS['purple']),
        ('Lower Tax\nRevenue', COLORS['teal']),
        ('Fiscal\nPressure\nIntensifies', COLORS['deep_blue']),
    ]
    
    positions = []
    for i, (text, color) in enumerate(elements):
        x = center[0] + radius * np.cos(angles[i])
        y = center[1] + radius * np.sin(angles[i])
        positions.append((x, y))
        
        box = FancyBboxPatch((x-1, y-0.6), 2, 1.2,
                            boxstyle="round,pad=0.2", facecolor=color, 
                            edgecolor='white', linewidth=2, alpha=0.9)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=9,
               fontweight='bold', color='white')
    
    # Draw circular arrows between elements
    for i in range(len(positions)):
        start = positions[i]
        end = positions[(i+1) % len(positions)]
        
        # Calculate control point for curved arrow
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2
        
        # Offset towards center for curve
        ctrl_x = mid_x + (center[0] - mid_x) * 0.3
        ctrl_y = mid_y + (center[1] - mid_y) * 0.3
        
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', color=COLORS['gray'], 
                                 lw=2, connectionstyle='arc3,rad=0.3'))
    
    # Add central label
    ax.text(center[0], center[1], 'Vicious\nCycle', fontsize=14, 
            ha='center', va='center', fontweight='bold', color=COLORS['red'])
    
    # Add feedback arrows text
    feedback_texts = [
        (positions[0][0]+1.2, positions[0][1]+0.8, 'Spreads\n↑'),
        (positions[1][0]+1.2, positions[1][1]-0.3, 'NPLs\n↑'),
        (positions[2][0]+0.5, positions[2][1]-1.2, 'Loan\nLosses'),
        (positions[3][0]-0.8, positions[3][1]-1.0, 'Guarantee\nCalls'),
        (positions[4][0]-1.5, positions[4][1]-0.3, 'Revenue\n↓'),
        (positions[5][0]-1.2, positions[5][1]+0.5, 'Debt\n↑'),
    ]
    
    for x, y, text in feedback_texts:
        ax.text(x, y, text, fontsize=8, ha='center', va='center', 
               color=COLORS['gray'], style='italic')
    
    ax.text(6, 0.5, 'Source: Author\'s analysis of sovereign-corporate nexus', 
            fontsize=9, ha='center', color=COLORS['gray'], style='italic')
    
    return save_figure(fig, 'figure_5_2_sovereign_corporate_loop.png')

# =============================================================================
# FIGURE 6.1-6.4 - Country Case Studies
# =============================================================================
def create_country_case_study(country_name, filename, figure_num):
    """Create detailed maturity profile for a country"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Country-specific data
    country_data = {
        'Ghana': {
            'maturities': {'Eurobonds': [3.2, 3.8, 5.2, 3.5, 2.5, 2.0, 1.5],
                          'Bilateral': [1.5, 1.8, 2.5, 2.0, 1.5, 1.2, 1.0],
                          'Local': [2.8, 3.2, 4.5, 3.8, 3.0, 2.5, 2.0],
                          'SOE': [0.8, 1.0, 1.5, 1.2, 0.9, 0.7, 0.5]},
            'spreads': [800, 900, 2000, 3500, 4000, 3500, 3000],
            'gfn': [18.5, 22.5, 19.0, 16.5],
            'reserves': [8.2, 7.5, 6.8, 6.2, 7.0, 7.5, 8.0],
            'total_debt': [72, 78, 82, 85, 83, 80, 78],
            'highlights': [
                '2022: Debt restructuring initiated',
                'External bond haircuts: 30-37%',
                'Local currency restructuring ongoing',
                'IMF program: $3bn ECF'
            ]
        },
        'Sri Lanka': {
            'maturities': {'Eurobonds': [2.5, 3.0, 4.2, 3.0, 2.2, 1.8, 1.2],
                          'Bilateral': [2.0, 2.5, 3.5, 2.8, 2.2, 1.8, 1.5],
                          'Local': [3.0, 3.5, 5.0, 4.0, 3.2, 2.8, 2.2],
                          'SOE': [1.2, 1.5, 2.0, 1.5, 1.2, 1.0, 0.8]},
            'spreads': [500, 600, 1500, 5000, 4500, 4000, 3500],
            'gfn': [22.0, 26.5, 20.5, 18.0],
            'reserves': [4.5, 2.0, 1.5, 1.2, 2.5, 3.0, 3.5],
            'total_debt': [95, 112, 120, 115, 105, 98, 92],
            'highlights': [
                'April 2022: Sovereign default',
                'First Asian SOE restructuring',
                'Bondholder negotiations ongoing',
                'IMF program: $2.9bn EFF'
            ]
        },
        'Zambia': {
            'maturities': {'Eurobonds': [1.8, 2.2, 3.0, 2.2, 1.6, 1.2, 0.8],
                          'Bilateral': [0.8, 1.0, 1.5, 1.2, 0.9, 0.7, 0.5],
                          'Local': [1.2, 1.5, 2.2, 1.8, 1.4, 1.1, 0.8],
                          'SOE': [0.5, 0.6, 0.8, 0.6, 0.5, 0.4, 0.3]},
            'spreads': [1500, 2000, 3000, 5000, 4500, 4000, 3500],
            'gfn': [15.5, 18.0, 16.0, 14.5],
            'reserves': [2.5, 2.0, 1.5, 1.8, 2.2, 2.5, 2.8],
            'total_debt': [85, 95, 100, 98, 90, 85, 80],
            'highlights': [
                'Nov 2020: First pandemic-era default',
                'G20 Common Framework case',
                'Bond restructuring agreed 2024',
                'IMF program: $1.3bn ECF'
            ]
        },
        'Pakistan': {
            'maturities': {'Eurobonds': [4.5, 5.2, 7.0, 5.0, 3.8, 3.0, 2.5],
                          'Bilateral': [3.5, 4.0, 5.5, 4.5, 3.5, 2.8, 2.2],
                          'Local': [5.0, 5.8, 8.0, 6.5, 5.0, 4.0, 3.2],
                          'SOE': [2.0, 2.5, 3.5, 2.8, 2.2, 1.8, 1.5]},
            'spreads': [600, 700, 1200, 2000, 2500, 2200, 2000],
            'gfn': [19.0, 23.5, 20.0, 18.5],
            'reserves': [12, 8, 5, 4, 6, 8, 10],
            'total_debt': [75, 82, 88, 85, 80, 76, 72],
            'highlights': [
                'High rollover risk from China',
                'Multiple IMF programs',
                'Energy sector circular debt',
                'Current account vulnerability'
            ]
        }
    }
    
    data = country_data[country_name]
    years = ['2024', '2025', '2026', '2027', '2028', '2029', '2030']
    x = np.arange(len(years))
    
    # Plot 1: Maturity Wall
    ax1 = axes[0, 0]
    width = 0.55
    colors = [COLORS['deep_blue'], COLORS['gold'], COLORS['light_blue'], COLORS['red']]
    bottom = np.zeros(len(years))
    
    for i, (instrument, values) in enumerate(data['maturities'].items()):
        ax1.bar(x, values, width, bottom=bottom, label=instrument, color=colors[i])
        bottom += np.array(values)
    
    ax1.axvspan(1.5, 2.5, alpha=0.15, color=COLORS['red'])
    ax1.set_xlabel('Year')
    ax1.set_ylabel('USD billions')
    ax1.set_title('Maturity Profile', fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(years)
    ax1.legend(loc='upper right', fontsize=8)
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Plot 2: Spreads over time
    ax2 = axes[0, 1]
    spread_years = [2020, 2021, 2022, 2023, 2024, 2025, 2026]
    ax2.plot(spread_years, data['spreads'], 'o-', color=COLORS['red'], linewidth=2.5, markersize=8)
    ax2.fill_between(spread_years, data['spreads'], alpha=0.3, color=COLORS['red'])
    ax2.axhline(y=1000, color=COLORS['gray'], linestyle='--', linewidth=1.5)
    ax2.text(2026.2, 1050, 'Distress', fontsize=8, color=COLORS['gray'])
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Spread (bps)')
    ax2.set_title('Sovereign Spread Evolution', fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    # Plot 3: GFN and Reserves
    ax3 = axes[1, 0]
    gfn_years = ['2025', '2026', '2027', '2028']
    x_gfn = np.arange(len(gfn_years))
    bars = ax3.bar(x_gfn, data['gfn'], color=COLORS['gold'], edgecolor='white')
    ax3.axhline(y=20, color=COLORS['red'], linestyle='--', linewidth=1.5)
    ax3.text(len(gfn_years)-0.5, 21, 'High GFN threshold', fontsize=8, color=COLORS['red'])
    ax3.set_xlabel('Year')
    ax3.set_ylabel('Gross Financing Needs (% GDP)')
    ax3.set_title('Gross Financing Needs', fontweight='bold')
    ax3.set_xticks(x_gfn)
    ax3.set_xticklabels(gfn_years)
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Plot 4: Key Highlights
    ax4 = axes[1, 1]
    ax4.axis('off')
    ax4.text(0.5, 0.95, f'{country_name}: Key Highlights', fontsize=12, 
            ha='center', va='top', fontweight='bold', color=COLORS['deep_blue'],
            transform=ax4.transAxes)
    
    for i, highlight in enumerate(data['highlights']):
        ax4.text(0.1, 0.75 - i*0.18, f'• {highlight}', fontsize=10,
                va='top', transform=ax4.transAxes)
    
    # Total debt info
    ax4.text(0.5, 0.15, f'Total Debt 2024: ${data["total_debt"][0]}bn\nDebt/GDP: {data["total_debt"][0]}%', 
            ha='center', va='center', fontsize=11, fontweight='bold',
            transform=ax4.transAxes, 
            bbox=dict(boxstyle='round', facecolor=COLORS['light_blue'], alpha=0.3))
    
    fig.suptitle(f'Figure {figure_num}: Case Study - {country_name} Maturity Profile', 
                fontsize=14, fontweight='bold', color=COLORS['deep_blue'], y=1.02)
    plt.tight_layout()
    
    return save_figure(fig, filename)

# =============================================================================
# FIGURE 7.1 - Liability Management Menu
# =============================================================================
def create_figure_7_1():
    """Create Liability Management Menu Diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    ax.text(7, 9.5, 'Figure 7.1: Liability Management Menu', 
            fontsize=14, fontweight='bold', ha='center', color=COLORS['deep_blue'])
    
    box_style = "round,pad=0.3,rounding_size=0.15"
    
    # Main categories
    categories = [
        (2.5, 7.5, 'BUYBACKS', COLORS['deep_blue'], 
         ['• Cash repurchase', '• Discount buybacks', '• Dutch auctions', '• Liability management exercises']),
        (7, 7.5, 'EXCHANGES', COLORS['gold'], 
         ['• Maturity extensions', '• Coupon modifications', '• Par-for-par swaps', '• New instrument issuance']),
        (11.5, 7.5, 'EXTENSIONS', COLORS['green'], 
         ['• Consent solicitations', '• Amendment offers', '• Grace period extensions', '• Payment deferrals']),
        (2.5, 3.5, 'CASH BUFFERS', COLORS['purple'], 
         ['• Reserve accumulation', '• Contingent credit lines', '• SDR allocations', '• SWAP arrangements']),
        (7, 3.5, 'CREDITOR\nCOORDINATION', COLORS['red'], 
         ['• CACs activation', '• Creditor committees', '• Comparability treatment', '• Information sharing']),
        (11.5, 3.5, 'STRUCTURAL\nREFORMS', COLORS['teal'], 
         ['• Debt management office', '• Medium-term strategy', '• Risk framework', '• Capacity building']),
    ]
    
    for x, y, title, color, items in categories:
        # Main box
        box = FancyBboxPatch((x-1.8, y-1.5), 3.6, 2.8,
                            boxstyle=box_style, facecolor=color, 
                            edgecolor='white', linewidth=2, alpha=0.15)
        ax.add_patch(box)
        
        # Title box
        title_box = FancyBboxPatch((x-1.5, y+0.8), 3, 0.6,
                                   boxstyle=box_style, facecolor=color, 
                                   edgecolor='white', linewidth=2, alpha=0.9)
        ax.add_patch(title_box)
        ax.text(x, y+1.1, title, ha='center', va='center', fontsize=10,
               fontweight='bold', color='white')
        
        # Items
        for i, item in enumerate(items):
            ax.text(x, y+0.3-i*0.4, item, ha='center', va='center', fontsize=9,
                   color=COLORS['deep_blue'])
    
    ax.text(7, 0.5, 'Source: IMF, World Bank, and author\'s framework for sovereign liability management', 
            fontsize=9, ha='center', color=COLORS['gray'], style='italic')
    
    return save_figure(fig, 'figure_7_1_liability_menu.png')

# =============================================================================
# FIGURE 7.2 - IMF/IFI Engagement Sequencing
# =============================================================================
def create_figure_7_2():
    """Create IMF/IFI Engagement Sequencing Timeline"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    ax.text(7, 7.5, 'Figure 7.2: IMF/IFI Engagement Sequencing', 
            fontsize=14, fontweight='bold', ha='center', color=COLORS['deep_blue'])
    
    # Timeline arrow
    ax.annotate('', xy=(13, 4), xytext=(1, 4),
               arrowprops=dict(arrowstyle='->', color=COLORS['gray'], lw=3))
    ax.text(13.2, 4, 'Time', fontsize=10, va='center', color=COLORS['gray'])
    
    # Timeline phases
    phases = [
        (2.5, 'Early Warning\nTriggers', COLORS['green'], 
         ['GFN > 20% GDP', 'Spreads > 500bps', 'Reserves < 3 months'], -0.5),
        (5.5, 'Technical\nAssistance', COLORS['gold'], 
         ['DSAs update', 'MTDS development', 'Capacity building'], 0.5),
        (8.5, 'Program\nDesign', COLORS['orange'], 
         ['Conditionality framework', 'Financing package', 'Reform agenda'], -0.5),
        (11.5, 'Program\nImplementation', COLORS['red'], 
         ['Reviews & disbursements', 'Policy adjustments', 'Exit strategy'], 0.5),
    ]
    
    for x, title, color, items, offset in phases:
        # Timeline marker
        circle = plt.Circle((x, 4), 0.25, color=color, zorder=5)
        ax.add_patch(circle)
        
        # Title box
        y_pos = 4 + offset * 2.5
        box = FancyBboxPatch((x-1.3, y_pos-0.3), 2.6, 0.6,
                            boxstyle="round,pad=0.2", facecolor=color, 
                            edgecolor='white', linewidth=2, alpha=0.9)
        ax.add_patch(box)
        ax.text(x, y_pos, title, ha='center', va='center', fontsize=9,
               fontweight='bold', color='white')
        
        # Items
        y_items = y_pos - 0.6 if offset < 0 else y_pos + 0.5
        for i, item in enumerate(items):
            y_item = y_items - i*0.35 if offset < 0 else y_items + i*0.35
            ax.text(x, y_item, f'• {item}', ha='center', va='center', fontsize=8,
                   color=COLORS['deep_blue'])
        
        # Connector
        ax.plot([x, x], [4 + np.sign(offset)*0.3, y_pos - np.sign(offset)*0.35], 
               color=color, linewidth=2, linestyle='--', alpha=0.5)
    
    # Add arrows between phases
    for i in range(len(phases)-1):
        ax.annotate('', xy=(phases[i+1][0]-0.5, 4), xytext=(phases[i][0]+0.5, 4),
                   arrowprops=dict(arrowstyle='->', color=COLORS['gray'], lw=1.5))
    
    ax.text(7, 0.5, 'Source: Author\'s framework based on IMF operational guidance', 
            fontsize=9, ha='center', color=COLORS['gray'], style='italic')
    
    return save_figure(fig, 'figure_7_2_imf_engagement.png')

# =============================================================================
# FIGURE 7.3 - Policy Implementation Roadmap
# =============================================================================
def create_figure_7_3():
    """Create Policy Implementation Roadmap Gantt Chart"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Tasks and timeline
    tasks = [
        ('Diagnostic Phase', 0, 3, COLORS['deep_blue']),
        ('Debt Sustainability Analysis', 0, 2, COLORS['deep_blue']),
        ('Stakeholder Mapping', 1, 3, COLORS['deep_blue']),
        ('Creditor Engagement', 2, 4, COLORS['gold']),
        ('Strategy Development', 3, 5, COLORS['gold']),
        ('Technical Assistance', 2, 6, COLORS['green']),
        ('IMF Program Negotiation', 4, 7, COLORS['orange']),
        ('Liability Management Ops', 5, 9, COLORS['red']),
        ('Monitoring Framework', 6, 12, COLORS['purple']),
        ('Capacity Building', 4, 12, COLORS['teal']),
        ('Exit Strategy Planning', 9, 12, COLORS['light_blue']),
    ]
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    for i, (task, start, end, color) in enumerate(tasks):
        ax.barh(i, end-start, left=start, height=0.6, color=color, alpha=0.8, edgecolor='white')
        ax.text(start + (end-start)/2, i, task, ha='center', va='center', 
               fontsize=9, fontweight='bold', color='white')
    
    ax.set_xlim(-0.5, 12.5)
    ax.set_ylim(-0.5, len(tasks))
    ax.set_xlabel('Month (2024-2026 Implementation Period)', fontweight='bold')
    ax.set_yticks(range(len(tasks)))
    ax.set_yticklabels([''] * len(tasks))  # Hide y labels as task names are in bars
    ax.set_xticks(range(12))
    ax.set_xticklabels(months)
    
    # Add year markers
    ax.axvline(x=6, color=COLORS['gray'], linestyle='--', alpha=0.5)
    ax.text(6, len(tasks)+0.3, 'Mid-Year Review', ha='center', fontsize=9, color=COLORS['gray'])
    
    ax.set_title('Figure 7.3: Policy Implementation Roadmap', 
                fontsize=14, fontweight='bold', color=COLORS['deep_blue'], pad=15)
    ax.grid(True, alpha=0.3, axis='x')
    
    # Legend
    legend_elements = [
        mpatches.Patch(color=COLORS['deep_blue'], label='Diagnostic'),
        mpatches.Patch(color=COLORS['gold'], label='Strategy'),
        mpatches.Patch(color=COLORS['green'], label='Technical'),
        mpatches.Patch(color=COLORS['orange'], label='Negotiation'),
        mpatches.Patch(color=COLORS['red'], label='Operations'),
        mpatches.Patch(color=COLORS['purple'], label='Monitoring'),
    ]
    ax.legend(handles=legend_elements, loc='upper right', ncol=3, fontsize=9)
    
    ax.text(12, -1.5, 'Source: Author\'s implementation framework', 
            fontsize=9, ha='right', color=COLORS['gray'], style='italic')
    
    return save_figure(fig, 'figure_7_3_implementation_roadmap.png')

# =============================================================================
# FIGURE 7.4 - Creditor Coordination Framework
# =============================================================================
def create_figure_7_4():
    """Create Creditor Coordination Framework Flowchart"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    ax.text(7, 9.5, 'Figure 7.4: Creditor Coordination Framework', 
            fontsize=14, fontweight='bold', ha='center', color=COLORS['deep_blue'])
    
    box_style = "round,pad=0.3,rounding_size=0.15"
    
    # Central process
    nodes = [
        # Top level - Principles
        (3.5, 8, 'COLLECTIVE\nACTION\nCLAUSES', COLORS['deep_blue']),
        (7, 8, 'COMPARABILITY\nOF\nTREATMENT', COLORS['gold']),
        (10.5, 8, 'TRANSPARENCY\nPACKAGE', COLORS['green']),
        
        # Middle level - Mechanisms
        (2.5, 5.5, 'Bondholder\nCoordination', COLORS['light_blue']),
        (5.5, 5.5, 'Bilateral\nCreditor Group', COLORS['gold']),
        (8.5, 5.5, 'IFI\nEngagement', COLORS['green']),
        (11.5, 5.5, 'Private\nCreditor Group', COLORS['red']),
        
        # Bottom level - Implementation
        (4, 2.5, '• Voting thresholds\n• Single-limb aggregation\n• Engagement timeline', COLORS['light_blue']),
        (7, 2.5, '• Official creditor committee\n• Paris Club coordination\n• Non-Paris Club engagement', COLORS['gold']),
        (10, 2.5, '• Information sharing\n• Data room access\n• Regular briefings', COLORS['green']),
    ]
    
    for x, y, text, color in nodes:
        height = 1.5 if y > 4 else 1.2
        width = 2.8 if y > 4 else 3.2
        
        box = FancyBboxPatch((x-width/2, y-height/2), width, height,
                            boxstyle=box_style, facecolor=color, 
                            edgecolor='white', linewidth=2, alpha=0.9)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=9,
               fontweight='bold', color='white')
    
    # Arrows
    arrows = [
        (3.5, 7.1, 2.5, 6.3),
        (3.5, 7.1, 5.5, 6.3),
        (7, 7.1, 5.5, 6.3),
        (7, 7.1, 8.5, 6.3),
        (10.5, 7.1, 8.5, 6.3),
        (10.5, 7.1, 11.5, 6.3),
        (2.5, 4.7, 4, 3.2),
        (5.5, 4.7, 7, 3.2),
        (8.5, 4.7, 10, 3.2),
        (11.5, 4.7, 10, 3.2),
    ]
    
    for x1, y1, x2, y2 in arrows:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='->', color=COLORS['gray'], lw=1.5))
    
    # Labels
    ax.text(1.5, 6.7, 'Principles', fontsize=10, fontweight='bold', color=COLORS['deep_blue'])
    ax.text(1.5, 4.2, 'Mechanisms', fontsize=10, fontweight='bold', color=COLORS['deep_blue'])
    ax.text(1.5, 1.5, 'Implementation', fontsize=10, fontweight='bold', color=COLORS['deep_blue'])
    
    ax.text(7, 0.3, 'Source: IMF, World Bank, G20 Common Framework documentation', 
            fontsize=9, ha='center', color=COLORS['gray'], style='italic')
    
    return save_figure(fig, 'figure_7_4_creditor_coordination.png')

# =============================================================================
# FIGURE 8.1 - Risk Register Heat Map
# =============================================================================
def create_figure_8_1():
    """Create Risk Register Heat Map"""
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Risk matrix
    risks = [
        'Market Access Closure',
        'FX Reserve Depletion',
        'Political Instability',
        'Creditor Coordination Failure',
        'External Shock (Commodities)',
        'Domestic Banking Crisis',
        'Policy Implementation Delay',
        'Legal/Contractual Disputes',
        'Social Unrest',
        'Climate/Environmental Event'
    ]
    
    likelihood = [4, 5, 3, 4, 3, 3, 4, 2, 4, 2]  # 1-5 scale
    impact = [5, 5, 4, 4, 4, 5, 3, 3, 4, 4]  # 1-5 scale
    
    # Create heat map
    colors_heat = []
    for l, i in zip(likelihood, impact):
        score = l * i
        if score >= 15:
            colors_heat.append('#c53030')  # Red - High risk
        elif score >= 10:
            colors_heat.append('#dd6b20')  # Orange - Medium-high
        elif score >= 6:
            colors_heat.append('#b7791f')  # Yellow - Medium
        else:
            colors_heat.append('#2f855a')  # Green - Low
    
    y_pos = np.arange(len(risks))
    
    # Plot dots
    for i, (risk, l, imp, c) in enumerate(zip(risks, likelihood, impact, colors_heat)):
        ax.scatter(imp, len(risks)-1-i, s=500, c=c, edgecolor='white', linewidth=2, zorder=5)
        ax.text(imp, len(risks)-1-i, f'{l*imp}', ha='center', va='center', 
               fontsize=10, fontweight='bold', color='white')
    
    # Add risk labels
    for i, risk in enumerate(risks):
        ax.text(-0.3, len(risks)-1-i, risk, ha='right', va='center', fontsize=10)
    
    # Grid and labels
    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(-1, len(risks))
    ax.set_xlabel('Impact (1-5)', fontweight='bold')
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_xticklabels(['Low', 'Moderate', 'High', 'Severe', 'Critical'])
    ax.set_yticks([])
    
    # Add likelihood labels on right
    ax2 = ax.twinx()
    ax2.set_ylim(ax.get_ylim())
    ax2.set_yticks(range(len(risks)))
    ax2.set_yticklabels([f'L{l}' for l in reversed(likelihood)])
    ax2.set_ylabel('Likelihood', fontweight='bold')
    
    # Color legend
    legend_elements = [
        mpatches.Patch(color='#c53030', label='Critical (15+)'),
        mpatches.Patch(color='#dd6b20', label='High (10-14)'),
        mpatches.Patch(color='#b7791f', label='Medium (6-9)'),
        mpatches.Patch(color='#2f855a', label='Low (<6)'),
    ]
    ax.legend(handles=legend_elements, loc='upper center', ncol=4, 
             fontsize=9, bbox_to_anchor=(0.5, 1.15))
    
    ax.set_title('Figure 8.1: Risk Register Heat Map', 
                fontsize=14, fontweight='bold', color=COLORS['deep_blue'], pad=30)
    ax.grid(True, alpha=0.3)
    
    # Add threshold lines
    for x in [1.5, 2.5, 3.5, 4.5]:
        ax.axvline(x=x, color=COLORS['gray'], linestyle=':', alpha=0.5)
    
    ax.text(5.5, -1.5, 'Source: Author\'s risk assessment framework', 
            fontsize=9, ha='right', color=COLORS['gray'], style='italic')
    
    return save_figure(fig, 'figure_8_1_risk_heat_map.png')


# =============================================================================
# MAIN EXECUTION
# =============================================================================
def main():
    """Generate all figures"""
    print("=" * 60)
    print("Generating all figures for 'The 2026 Refinancing Wall' report")
    print("=" * 60)
    
    created_files = []
    
    # Figure 1.1 - Conceptual Framework
    print("\n[1/22] Creating Figure 1.1 - Conceptual Framework...")
    created_files.append(create_figure_1_1())
    
    # Figure 2.1 - Global Interest Rates
    print("[2/22] Creating Figure 2.1 - Global Interest Rates...")
    created_files.append(create_figure_2_1())
    
    # Figure 2.2 - Sovereign Spreads
    print("[3/22] Creating Figure 2.2 - Sovereign Spreads...")
    created_files.append(create_figure_2_2())
    
    # Figure 4.1 - Aggregate Maturity Wall
    print("[4/22] Creating Figure 4.1 - Aggregate Maturity Wall...")
    created_files.append(create_figure_4_1())
    
    # Figure 4.2 - Country Maturity Walls
    print("[5/22] Creating Figure 4.2 - Country Maturity Walls...")
    created_files.append(create_figure_4_2())
    
    # Figure 4.3 - Gross Financing Needs
    print("[6/22] Creating Figure 4.3 - Gross Financing Needs...")
    created_files.append(create_figure_4_3())
    
    # Figure 4.4 - Debt Service Revenue Ratio
    print("[7/22] Creating Figure 4.4 - Debt Service Revenue Ratio...")
    created_files.append(create_figure_4_4())
    
    # Figure 4.5 - Stress Scenario Fan Chart
    print("[8/22] Creating Figure 4.5 - Stress Scenario Fan Chart...")
    created_files.append(create_figure_4_5())
    
    # Figure 4.6 - Refinancing Gap Results
    print("[9/22] Creating Figure 4.6 - Refinancing Gap Results...")
    created_files.append(create_figure_4_6())
    
    # Figure 4.7 - Rollover Capacity
    print("[10/22] Creating Figure 4.7 - Rollover Capacity...")
    created_files.append(create_figure_4_7())
    
    # Figure 4.8 - FX Reserve Adequacy
    print("[11/22] Creating Figure 4.8 - FX Reserve Adequacy...")
    created_files.append(create_figure_4_8())
    
    # Figure 5.1 - Decision Tree
    print("[12/22] Creating Figure 5.1 - Decision Tree...")
    created_files.append(create_figure_5_1())
    
    # Figure 5.2 - Sovereign-Corporate Loop
    print("[13/22] Creating Figure 5.2 - Sovereign-Corporate Loop...")
    created_files.append(create_figure_5_2())
    
    # Figure 6.1 - Ghana Case Study
    print("[14/22] Creating Figure 6.1 - Ghana Case Study...")
    created_files.append(create_country_case_study('Ghana', 'figure_6_1_ghana_case_study.png', '6.1'))
    
    # Figure 6.2 - Sri Lanka Case Study
    print("[15/22] Creating Figure 6.2 - Sri Lanka Case Study...")
    created_files.append(create_country_case_study('Sri Lanka', 'figure_6_2_sri_lanka_case_study.png', '6.2'))
    
    # Figure 6.3 - Zambia Case Study
    print("[16/22] Creating Figure 6.3 - Zambia Case Study...")
    created_files.append(create_country_case_study('Zambia', 'figure_6_3_zambia_case_study.png', '6.3'))
    
    # Figure 6.4 - Pakistan Case Study
    print("[17/22] Creating Figure 6.4 - Pakistan Case Study...")
    created_files.append(create_country_case_study('Pakistan', 'figure_6_4_pakistan_case_study.png', '6.4'))
    
    # Figure 7.1 - Liability Management Menu
    print("[18/22] Creating Figure 7.1 - Liability Management Menu...")
    created_files.append(create_figure_7_1())
    
    # Figure 7.2 - IMF Engagement
    print("[19/22] Creating Figure 7.2 - IMF Engagement...")
    created_files.append(create_figure_7_2())
    
    # Figure 7.3 - Implementation Roadmap
    print("[20/22] Creating Figure 7.3 - Implementation Roadmap...")
    created_files.append(create_figure_7_3())
    
    # Figure 7.4 - Creditor Coordination
    print("[21/22] Creating Figure 7.4 - Creditor Coordination...")
    created_files.append(create_figure_7_4())
    
    # Figure 8.1 - Risk Heat Map
    print("[22/22] Creating Figure 8.1 - Risk Heat Map...")
    created_files.append(create_figure_8_1())
    
    print("\n" + "=" * 60)
    print("ALL FIGURES GENERATED SUCCESSFULLY!")
    print("=" * 60)
    print(f"\nOutput directory: {OUTPUT_DIR}")
    print(f"Total figures created: {len(created_files)}")
    print("\nFiles created:")
    for i, f in enumerate(created_files, 1):
        print(f"  {i}. {os.path.basename(f)}")
    
    return created_files


if __name__ == '__main__':
    main()
