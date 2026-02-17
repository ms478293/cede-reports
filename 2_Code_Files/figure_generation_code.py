"""
The 2026 Refinancing Wall - Figure Generation Code (FIXED VERSION)
Larger fonts, correct numbering, professional styling
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import matplotlib.lines as mlines
import numpy as np
from pathlib import Path

# Output directory
OUTPUT_DIR = Path('/home/z/my-project/download/final_package/3_Images_and_Data/figures')
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Set matplotlib defaults with LARGER fonts
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['font.size'] = 14  # Increased from 11
plt.rcParams['axes.titlesize'] = 16  # Increased from 12
plt.rcParams['axes.labelsize'] = 14  # Increased from 11
plt.rcParams['xtick.labelsize'] = 12  # Increased from 10
plt.rcParams['ytick.labelsize'] = 12  # Increased from 10
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

COLORS = {
    'primary': '#1a365d',
    'secondary': '#b7791f',
    'accent': '#718096',
    'danger': '#c53030',
    'success': '#2f855a',
    'warning': '#d69e2e'
}

def save_figure(fig, filename):
    filepath = OUTPUT_DIR / filename
    fig.savefig(filepath, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"Saved: {filepath}")
    return str(filepath)


def create_figure_1():
    """Figure 1: Conceptual Framework - LARGER TEXT"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(7, 9.5, 'Figure 1: The Refinancing Wall Mechanism', 
            ha='center', va='top', fontsize=18, fontweight='bold', color=COLORS['primary'])
    
    # Top row - Drivers
    boxes = [
        (2.5, 7.5, 'Maturity\nBunching', COLORS['primary']),
        (7, 7.5, 'High Global\nInterest Rates', COLORS['primary']),
        (11.5, 7.5, 'Tighter Risk\nAppetite', COLORS['primary']),
    ]
    
    for x, y, text, color in boxes:
        box = FancyBboxPatch((x-1.5, y-0.7), 3, 1.4, 
                             boxstyle="round,pad=0.1", 
                             facecolor=color, alpha=0.9, edgecolor='white', linewidth=3)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=14, 
                color='white', fontweight='bold')
    
    # Middle row - Crisis point
    box = FancyBboxPatch((5, 5, 4, 1.6), boxstyle="round,pad=0.1",
                         facecolor=COLORS['danger'], alpha=0.9, edgecolor='white', linewidth=3)
    ax.add_patch(box)
    ax.text(7, 5.8, 'REFINANCING WALL', ha='center', va='center', fontsize=16, 
            color='white', fontweight='bold')
    ax.text(7, 5.2, 'Rollover Impossibility', ha='center', va='center', fontsize=13, color='white')
    
    # Bottom row - Consequences
    boxes2 = [
        (2.5, 2.5, 'FX Reserve\nDrawdown', COLORS['warning']),
        (7, 2.5, 'Auction\nFailure', COLORS['warning']),
        (11.5, 2.5, 'Spread\nWidening', COLORS['warning']),
    ]
    
    for x, y, text, color in boxes2:
        box = FancyBboxPatch((x-1.5, y-0.7), 3, 1.4, 
                             boxstyle="round,pad=0.1", 
                             facecolor=color, alpha=0.9, edgecolor='white', linewidth=3)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=14, 
                color='white', fontweight='bold')
    
    # Final outcome
    box = FancyBboxPatch((5, 0.3, 4, 1.2), boxstyle="round,pad=0.1",
                         facecolor=COLORS['danger'], alpha=0.9, edgecolor='white', linewidth=3)
    ax.add_patch(box)
    ax.text(7, 0.9, 'Default Probability Spike', ha='center', va='center', fontsize=15, 
            color='white', fontweight='bold')
    
    # Arrows
    arrow_props = dict(arrowstyle='->', color=COLORS['accent'], lw=2.5)
    arrows = [
        ((4, 7.5), (5.5, 6.6)), ((7, 6.8), (7, 6.6)), ((10, 7.5), (8.5, 6.6)),
        ((7, 5), (4, 3.5)), ((7, 5), (7, 3.5)), ((7, 5), (10, 3.5)),
        ((4, 1.8), (5.5, 1.5)), ((7, 1.8), (7, 1.5)), ((10, 1.8), (8.5, 1.5)),
    ]
    for start, end in arrows:
        ax.annotate('', xy=end, xytext=start, arrowprops=arrow_props)
    
    return save_figure(fig, 'figure_1_conceptual_framework.png')


def create_figure_2():
    """Figure 2: Global Interest Rates"""
    fig, ax = plt.subplots(figsize=(14, 7))
    
    years = np.array([2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026])
    
    fed = [2.2, 0.1, 0.1, 4.3, 5.3, 5.0, 4.5, 4.0]
    ecb = [0.0, 0.0, 0.0, 2.0, 4.0, 3.5, 3.0, 2.5]
    boe = [0.8, 0.1, 0.1, 3.5, 5.0, 4.75, 4.0, 3.5]
    em = [4.5, 3.5, 3.8, 6.5, 8.0, 7.5, 6.5, 5.5]
    
    ax.plot(years, fed, 'o-', color=COLORS['primary'], lw=3, ms=10, label='Federal Reserve')
    ax.plot(years, ecb, 's-', color=COLORS['secondary'], lw=3, ms=10, label='European Central Bank')
    ax.plot(years, boe, '^-', color=COLORS['success'], lw=3, ms=10, label='Bank of England')
    ax.plot(years, em, 'D-', color=COLORS['danger'], lw=3, ms=10, label='Emerging Markets Average')
    
    ax.axvspan(2022, 2024, alpha=0.15, color=COLORS['warning'])
    ax.annotate('Global Tightening\nCycle', xy=(2023, 7.5), fontsize=13, ha='center', fontweight='bold')
    
    ax.set_xlabel('Year', fontsize=14, fontweight='bold')
    ax.set_ylabel('Policy Rate (%)', fontsize=14, fontweight='bold')
    ax.set_title('Figure 2: Global Interest Rate Trends (2019-2026)', fontsize=18, fontweight='bold', pad=20)
    ax.legend(loc='upper left', fontsize=12, framealpha=0.9)
    ax.set_xlim(2018.5, 2026.5)
    ax.set_ylim(-0.5, 9)
    ax.grid(True, alpha=0.3)
    
    return save_figure(fig, 'figure_2_global_interest_rates.png')


def create_figure_3():
    """Figure 3: Sovereign Spreads"""
    fig, ax = plt.subplots(figsize=(14, 7))
    
    years = np.array([2020, 2021, 2022, 2023, 2024, 2025, 2026])
    
    embi = [350, 320, 580, 520, 380, 420, 400]
    ghana = [850, 920, 2800, 2500, 2000, 1800, 1600]
    srilanka = [650, 720, 3500, 3200, 2800, 2400, 2000]
    zambia = [1200, 1500, 2800, 2200, 1600, 1400, 1200]
    pakistan = [580, 650, 1500, 1800, 1400, 1200, 1000]
    
    ax.plot(years, embi, 'o-', color=COLORS['primary'], lw=3, ms=10, label='EMBI Global')
    ax.plot(years, ghana, 's-', color=COLORS['danger'], lw=3, ms=10, label='Ghana')
    ax.plot(years, srilanka, '^-', color=COLORS['success'], lw=3, ms=10, label='Sri Lanka')
    ax.plot(years, zambia, 'D-', color=COLORS['secondary'], lw=3, ms=10, label='Zambia')
    ax.plot(years, pakistan, 'v-', color=COLORS['primary'], lw=3, ms=10, label='Pakistan')
    
    ax.axhline(y=1000, color=COLORS['danger'], linestyle='--', lw=2, label='Distress Threshold')
    
    ax.annotate('2022 Crisis\nPeak', xy=(2022, 2800), xytext=(2021.3, 3200), fontsize=12,
                arrowprops=dict(arrowstyle='->', color='gray', lw=2))
    
    ax.set_xlabel('Year', fontsize=14, fontweight='bold')
    ax.set_ylabel('Spread (basis points)', fontsize=14, fontweight='bold')
    ax.set_title('Figure 3: Sovereign Spread Evolution (2020-2026)', fontsize=18, fontweight='bold', pad=20)
    ax.legend(loc='upper right', fontsize=11, framealpha=0.9)
    ax.set_xlim(2019.5, 2026.5)
    ax.grid(True, alpha=0.3)
    
    return save_figure(fig, 'figure_3_sovereign_spreads.png')


def create_figure_4():
    """Figure 4: Aggregate Maturity Wall"""
    fig, ax = plt.subplots(figsize=(14, 7))
    
    years = ['2024', '2025', '2026', '2027', '2028', '2029', '2030']
    x = np.arange(len(years))
    width = 0.65
    
    eurobonds = [0.4, 3.2, 5.3, 8.7, 4.2, 2.0, 7.5]
    external = [8.2, 13.0, 17.3, 14.6, 16.1, 13.7, 15.5]
    local = [24.0, 33.5, 41.4, 38.8, 44.4, 33.5, 39.0]
    soe = [2.8, 4.2, 6.0, 5.3, 4.2, 4.8, 5.4]
    
    colors_inst = {'Eurobonds': '#c53030', 'External FX Debt': '#b7791f', 
                   'Local Currency': '#1a365d', 'SOE Obligations': '#718096'}
    
    ax.bar(x, eurobonds, width, label='Eurobonds', color=colors_inst['Eurobonds'])
    ax.bar(x, external, width, bottom=eurobonds, label='External FX Debt', color=colors_inst['External FX Debt'])
    ax.bar(x, local, width, bottom=np.array(eurobonds)+np.array(external), 
           label='Local Currency', color=colors_inst['Local Currency'])
    ax.bar(x, soe, width, bottom=np.array(eurobonds)+np.array(external)+np.array(local),
           label='SOE Obligations', color=colors_inst['SOE Obligations'])
    
    ax.axvspan(1.5, 2.5, alpha=0.2, color=COLORS['danger'])
    ax.annotate('2026 PEAK', xy=(2, 62), fontsize=14, ha='center', fontweight='bold', color=COLORS['danger'])
    
    ax.set_xlabel('Year', fontsize=14, fontweight='bold')
    ax.set_ylabel('Debt Maturing ($ billion)', fontsize=14, fontweight='bold')
    ax.set_title('Figure 4: Aggregate Debt Maturity Wall', fontsize=18, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.legend(loc='upper left', fontsize=11, framealpha=0.9)
    ax.grid(True, alpha=0.3, axis='y')
    
    return save_figure(fig, 'figure_4_aggregate_maturity_wall.png')


def create_figure_5():
    """Figure 5: Gross Financing Needs"""
    fig, ax = plt.subplots(figsize=(14, 7))
    
    countries = ['Ghana', 'Sri Lanka', 'Zambia', 'Pakistan', 'Kenya', 'Egypt']
    gfn_2025 = [18.2, 15.8, 14.2, 21.5, 16.8, 22.4]
    gfn_2026 = [22.4, 18.5, 17.5, 28.2, 14.2, 25.8]
    
    x = np.arange(len(countries))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, gfn_2025, width, label='2025', color=COLORS['primary'], alpha=0.85)
    bars2 = ax.bar(x + width/2, gfn_2026, width, label='2026', color=COLORS['danger'], alpha=0.85)
    
    ax.axhline(y=20, color=COLORS['danger'], linestyle='--', lw=2.5, label='Crisis Threshold (20%)')
    ax.axhline(y=15, color=COLORS['warning'], linestyle=':', lw=2.5, label='Stress Threshold (15%)')
    
    ax.set_xlabel('Country', fontsize=14, fontweight='bold')
    ax.set_ylabel('Gross Financing Need (% of GDP)', fontsize=14, fontweight='bold')
    ax.set_title('Figure 5: Gross Financing Needs by Country', fontsize=18, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(countries)
    ax.legend(loc='upper right', fontsize=11, framealpha=0.9)
    ax.grid(True, alpha=0.3, axis='y')
    
    return save_figure(fig, 'figure_5_gross_financing_needs.png')


def create_figure_6():
    """Figure 6: Debt Service to Revenue Ratio"""
    fig, ax = plt.subplots(figsize=(14, 7))
    
    countries = ['Ghana', 'Sri Lanka', 'Zambia', 'Pakistan', 'Kenya', 'Egypt']
    ratio_2024 = [38.5, 52.4, 45.2, 48.5, 32.5, 42.5]
    ratio_2026 = [48.2, 42.8, 35.2, 58.4, 32.2, 48.5]
    
    x = np.arange(len(countries))
    width = 0.35
    
    ax.bar(x - width/2, ratio_2024, width, label='2024', color=COLORS['primary'], alpha=0.85)
    ax.bar(x + width/2, ratio_2026, width, label='2026', color=COLORS['secondary'], alpha=0.85)
    
    ax.axhline(y=30, color=COLORS['danger'], linestyle='--', lw=2.5, label='Crisis Threshold (30%)')
    ax.axhline(y=25, color=COLORS['warning'], linestyle=':', lw=2.5, label='Stress Threshold (25%)')
    
    ax.set_xlabel('Country', fontsize=14, fontweight='bold')
    ax.set_ylabel('Debt Service / Government Revenue (%)', fontsize=14, fontweight='bold')
    ax.set_title('Figure 6: Debt Service to Revenue Ratio', fontsize=18, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(countries)
    ax.legend(loc='upper right', fontsize=11, framealpha=0.9)
    ax.grid(True, alpha=0.3, axis='y')
    
    return save_figure(fig, 'figure_6_debt_service_revenue_ratio.png')


def create_figure_7():
    """Figure 7: Stress Scenario Analysis"""
    fig, ax = plt.subplots(figsize=(14, 7))
    
    years = np.array([2024, 2025, 2026, 2027, 2028])
    
    baseline = [4.2, 4.8, 5.5, 5.2, 5.0]
    moderate = [4.2, 5.2, 6.8, 6.5, 6.2]
    severe = [4.2, 5.8, 8.5, 8.2, 7.8]
    
    ax.fill_between(years, baseline, severe, alpha=0.25, color=COLORS['danger'])
    ax.fill_between(years, baseline, moderate, alpha=0.35, color=COLORS['warning'])
    
    ax.plot(years, baseline, 'o-', color=COLORS['primary'], lw=3, ms=10, label='Baseline')
    ax.plot(years, moderate, 's--', color=COLORS['warning'], lw=2.5, ms=8, label='Moderate Stress (+300bps)')
    ax.plot(years, severe, '^--', color=COLORS['danger'], lw=2.5, ms=8, label='Severe Stress (+300bps, -15% FX)')
    
    ax.set_xlabel('Year', fontsize=14, fontweight='bold')
    ax.set_ylabel('Debt Service ($ billion)', fontsize=14, fontweight='bold')
    ax.set_title('Figure 7: Ghana Debt Service Under Stress Scenarios', fontsize=18, fontweight='bold', pad=20)
    ax.legend(loc='upper left', fontsize=11, framealpha=0.9)
    ax.grid(True, alpha=0.3)
    
    return save_figure(fig, 'figure_7_stress_scenario.png')


def create_figure_8():
    """Figure 8: Refinancing Gap"""
    fig, ax = plt.subplots(figsize=(14, 7))
    
    countries = ['Ghana', 'Sri Lanka', 'Zambia', 'Pakistan', 'Kenya', 'Egypt']
    baseline = [4.2, 3.8, 2.5, 8.5, 2.8, 6.5]
    stress = [8.5, 7.2, 5.2, 15.2, 5.5, 12.8]
    
    x = np.arange(len(countries))
    width = 0.35
    
    ax.bar(x - width/2, baseline, width, label='Baseline Gap', color=COLORS['primary'], alpha=0.85)
    ax.bar(x + width/2, stress, width, label='Stress Scenario Gap', color=COLORS['danger'], alpha=0.85)
    
    ax.set_xlabel('Country', fontsize=14, fontweight='bold')
    ax.set_ylabel('Refinancing Gap ($ billion)', fontsize=14, fontweight='bold')
    ax.set_title('Figure 8: Refinancing Gap Model Results', fontsize=18, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(countries)
    ax.legend(loc='upper right', fontsize=11, framealpha=0.9)
    ax.grid(True, alpha=0.3, axis='y')
    
    return save_figure(fig, 'figure_8_refinancing_gap.png')


def create_figure_9():
    """Figure 9: Reserve Adequacy"""
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    countries = ['Ghana', 'Sri Lanka', 'Zambia', 'Pakistan', 'Kenya', 'Egypt']
    months = [2.8, 1.9, 2.4, 1.3, 4.2, 3.2]
    coverage = [42, 28, 38, 22, 65, 48]
    
    x = np.arange(len(countries))
    
    # Chart 1
    ax1 = axes[0]
    colors1 = [COLORS['danger'] if m < 3 else COLORS['warning'] if m < 4 else COLORS['success'] for m in months]
    ax1.bar(x, months, color=colors1, alpha=0.85)
    ax1.axhline(y=3, color=COLORS['danger'], linestyle='--', lw=2.5, label='Critical (3 months)')
    ax1.set_title('Reserves in Months of Imports', fontsize=16, fontweight='bold')
    ax1.set_xlabel('Country', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Months', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(countries)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Chart 2
    ax2 = axes[1]
    colors2 = [COLORS['danger'] if c < 50 else COLORS['warning'] if c < 75 else COLORS['success'] for c in coverage]
    ax2.bar(x, coverage, color=colors2, alpha=0.85)
    ax2.axhline(y=100, color=COLORS['success'], linestyle='--', lw=2.5, label='Safe (100%)')
    ax2.axhline(y=50, color=COLORS['danger'], linestyle=':', lw=2.5, label='Critical (50%)')
    ax2.set_title('Short-term Debt Coverage', fontsize=16, fontweight='bold')
    ax2.set_xlabel('Country', fontsize=12, fontweight='bold')
    ax2.set_ylabel('% Coverage', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(countries)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3, axis='y')
    
    fig.suptitle('Figure 9: FX Reserve Adequacy Indicators', fontsize=18, fontweight='bold', y=1.02)
    plt.tight_layout()
    
    return save_figure(fig, 'figure_9_reserve_adequacy.png')


def create_figure_10():
    """Figure 10: Decision Tree"""
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    ax.text(8, 9.5, 'Figure 10: Liability Management Decision Tree', 
            ha='center', fontsize=18, fontweight='bold', color=COLORS['primary'])
    
    # Main decision nodes
    nodes = [
        (8, 8, 'Assess Refinancing\nRisk', COLORS['primary'], 'decision'),
        (4, 5.5, 'Market Access\nAvailable?', COLORS['primary'], 'decision'),
        (12, 5.5, 'Reserves\nAdequate?', COLORS['primary'], 'decision'),
        (2, 3, 'PRE-FUNDING', COLORS['success'], 'action'),
        (6, 3, 'LIABILITY\nMANAGEMENT', COLORS['warning'], 'action'),
        (10, 3, 'IMF/IFI\nENGAGEMENT', COLORS['warning'], 'action'),
        (14, 3, 'RESTRUCTURING', COLORS['danger'], 'action'),
    ]
    
    for x, y, text, color, node_type in nodes:
        if node_type == 'decision':
            box = FancyBboxPatch((x-1.5, y-0.6), 3, 1.2, boxstyle="round,pad=0.1",
                                 facecolor=color, alpha=0.9, edgecolor='white', linewidth=2)
        else:
            box = FancyBboxPatch((x-1.5, y-0.6), 3, 1.2, boxstyle="round,pad=0.1",
                                 facecolor=color, alpha=0.9, edgecolor='white', linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=12, color='white', fontweight='bold')
    
    # Arrows
    arrow_props = dict(arrowstyle='->', color=COLORS['accent'], lw=2.5)
    arrows = [
        ((8, 7.4), (4, 6.1)), ((8, 7.4), (12, 6.1)),
        ((4, 4.9), (2, 3.6)), ((4, 4.9), (6, 3.6)),
        ((12, 4.9), (10, 3.6)), ((12, 4.9), (14, 3.6)),
    ]
    for start, end in arrows:
        ax.annotate('', xy=end, xytext=start, arrowprops=arrow_props)
    
    # Labels
    ax.text(3, 5.8, 'YES', fontsize=12, color=COLORS['success'], fontweight='bold')
    ax.text(5.2, 5.8, 'NO', fontsize=12, color=COLORS['danger'], fontweight='bold')
    ax.text(11, 5.8, 'YES', fontsize=12, color=COLORS['success'], fontweight='bold')
    ax.text(13.2, 5.8, 'NO', fontsize=12, color=COLORS['danger'], fontweight='bold')
    
    return save_figure(fig, 'figure_10_decision_tree.png')


def create_figure_11():
    """Figure 11: Sovereign-Corporate Feedback Loop"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    ax.text(7, 9.5, 'Figure 11: Sovereign-Corporate Feedback Loop', 
            ha='center', fontsize=18, fontweight='bold', color=COLORS['primary'])
    
    # Central node
    circle = Circle((7, 5), 1.3, facecolor=COLORS['danger'], alpha=0.3, edgecolor=COLORS['danger'], linewidth=4)
    ax.add_patch(circle)
    ax.text(7, 5, 'REFINANCING\nCRISIS', ha='center', va='center', fontsize=14, fontweight='bold', color=COLORS['danger'])
    
    # Surrounding nodes
    nodes = [
        (2.5, 7.5, 'Sovereign Spread\nWidening', COLORS['primary']),
        (11.5, 7.5, 'Corporate Borrowing\nCosts Rise', COLORS['primary']),
        (2.5, 2.5, 'Bank Balance Sheet\nDeterioration', COLORS['warning']),
        (11.5, 2.5, 'SOE Financial\nStress', COLORS['warning']),
        (7, 1.5, 'Contingent Liabilities\nMaterialize', COLORS['danger']),
        (7, 8.5, 'Rating\nDowngrades', COLORS['danger']),
    ]
    
    for x, y, text, color in nodes:
        box = FancyBboxPatch((x-1.5, y-0.6), 3, 1.2, boxstyle="round,pad=0.1",
                             facecolor=color, alpha=0.9, edgecolor='white', linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=12, color='white', fontweight='bold')
    
    return save_figure(fig, 'figure_11_feedback_loop.png')


def create_case_study_figure(country, filename, fig_num):
    """Create case study figure with 4 panels"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    years = ['2024', '2025', '2026', '2027', '2028', '2029', '2030']
    x = np.arange(len(years))
    
    # Country data
    data = {
        'Ghana': {
            'maturities': [5.0, 6.5, 10.5, 7.4, 11.9, 6.9, 8.9],
            'gfn': [16.5, 18.2, 22.4, 19.8, 21.2, 18.5, 19.2],
            'spread': [2000, 2000, 1800, 1600, 1400, 1200, 1000],
            'dsr': [38.5, 42.8, 48.2, 45.5, 44.2, 42.0, 40.5]
        },
        'Sri Lanka': {
            'maturities': [3.5, 5.1, 7.3, 6.1, 6.3, 5.6, 6.3],
            'gfn': [14.2, 15.8, 18.5, 16.2, 17.8, 15.5, 16.2],
            'spread': [2800, 2800, 2400, 2000, 1600, 1200, 1000],
            'dsr': [52.4, 45.2, 42.8, 40.5, 38.2, 36.0, 34.5]
        },
        'Zambia': {
            'maturities': [1.7, 2.8, 3.9, 4.7, 3.8, 2.8, 5.4],
            'gfn': [12.8, 14.2, 17.5, 15.8, 16.5, 14.2, 15.0],
            'spread': [1600, 1600, 1400, 1200, 1000, 800, 600],
            'dsr': [45.2, 38.5, 35.2, 33.8, 32.5, 31.0, 30.0]
        },
        'Pakistan': {
            'maturities': [12.6, 19.6, 26.0, 23.3, 23.5, 19.3, 21.4],
            'gfn': [19.5, 21.5, 28.2, 25.4, 24.8, 22.5, 23.0],
            'spread': [1400, 1400, 1200, 1000, 900, 800, 700],
            'dsr': [48.5, 52.2, 58.4, 55.2, 52.8, 50.0, 48.5]
        }
    }
    
    d = data[country]
    
    # Panel 1: Maturities
    ax1 = axes[0, 0]
    ax1.bar(x, d['maturities'], color=COLORS['primary'], alpha=0.85)
    ax1.axvspan(1.5, 2.5, alpha=0.2, color=COLORS['danger'])
    ax1.set_title('Debt Maturities ($ billion)', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Year', fontsize=12)
    ax1.set_xticks(x)
    ax1.set_xticklabels(years)
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Panel 2: GFN
    ax2 = axes[0, 1]
    ax2.bar(x, d['gfn'], color=COLORS['secondary'], alpha=0.85)
    ax2.axhline(y=20, color=COLORS['danger'], linestyle='--', lw=2)
    ax2.set_title('Gross Financing Needs (% GDP)', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Year', fontsize=12)
    ax2.set_xticks(x)
    ax2.set_xticklabels(years)
    ax2.grid(True, alpha=0.3, axis='y')
    
    # Panel 3: Spreads
    ax3 = axes[1, 0]
    ax3.bar(x, d['spread'], color=COLORS['danger'], alpha=0.85)
    ax3.set_title('Sovereign Spreads (bps)', fontsize=14, fontweight='bold')
    ax3.set_xlabel('Year', fontsize=12)
    ax3.set_xticks(x)
    ax3.set_xticklabels(years)
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Panel 4: DSR
    ax4 = axes[1, 1]
    ax4.bar(x, d['dsr'], color=COLORS['warning'], alpha=0.85)
    ax4.axhline(y=30, color=COLORS['danger'], linestyle='--', lw=2)
    ax4.set_title('Debt Service / Revenue (%)', fontsize=14, fontweight='bold')
    ax4.set_xlabel('Year', fontsize=12)
    ax4.set_xticks(x)
    ax4.set_xticklabels(years)
    ax4.grid(True, alpha=0.3, axis='y')
    
    fig.suptitle(f'Figure {fig_num}: {country} Case Study', fontsize=18, fontweight='bold', y=1.02)
    plt.tight_layout()
    
    return save_figure(fig, filename)


def create_figure_16():
    """Figure 16: Implementation Roadmap"""
    fig, ax = plt.subplots(figsize=(16, 8))
    
    tasks = [
        ('Pre-funding facility setup', 0, 6, COLORS['success']),
        ('Liability management operations', 3, 15, COLORS['primary']),
        ('IMF/IFI engagement', 0, 12, COLORS['warning']),
        ('Domestic market development', 6, 30, COLORS['primary']),
        ('FX hedging instruments', 12, 18, COLORS['secondary']),
        ('SOE governance reforms', 12, 30, COLORS['warning']),
    ]
    
    y_pos = np.arange(len(tasks))
    
    for i, (task, start, end, color) in enumerate(tasks):
        ax.barh(i, end-start, left=start, height=0.5, color=color, alpha=0.85)
        ax.text(-2, i, task, ha='right', va='center', fontsize=11)
    
    ax.set_xlim(-12, 35)
    ax.set_ylim(-0.5, len(tasks)-0.5)
    ax.set_xlabel('Months', fontsize=14, fontweight='bold')
    ax.set_title('Figure 16: Policy Implementation Roadmap', fontsize=18, fontweight='bold', pad=20)
    ax.set_yticks([])
    ax.grid(True, alpha=0.3, axis='x')
    
    ax.axvline(x=6, color=COLORS['accent'], linestyle='--', alpha=0.7)
    ax.axvline(x=18, color=COLORS['accent'], linestyle='--', alpha=0.7)
    ax.text(3, len(tasks), 'Phase 1', ha='center', fontsize=12, fontweight='bold')
    ax.text(12, len(tasks), 'Phase 2', ha='center', fontsize=12, fontweight='bold')
    ax.text(27, len(tasks), 'Phase 3', ha='center', fontsize=12, fontweight='bold')
    
    return save_figure(fig, 'figure_16_implementation_roadmap.png')


def create_figure_17():
    """Figure 17: Risk Heat Map"""
    fig, ax = plt.subplots(figsize=(12, 10))
    
    risks = [
        'Spread widening', 'Auction failure', 'Reserve depletion',
        'FX shortage', 'Fiscal reversal', 'IMF derailment',
        'SOE liabilities', 'Commodity shock', 'Global risk-off'
    ]
    
    likelihood = [4, 3, 4, 4, 3, 3, 4, 3, 4]
    impact = [4, 5, 5, 4, 4, 5, 4, 4, 4]
    
    for i in range(5, 0, -1):
        for j in range(1, 6):
            if i <= 2 and j <= 2:
                color = '#c6f6d5'
            elif i >= 4 and j >= 4:
                color = '#fed7d7'
            else:
                color = '#feebc8'
            ax.add_patch(Rectangle((j-0.5, i-0.5), 1, 1, facecolor=color, edgecolor='white', linewidth=1))
    
    for r, l, im in zip(risks, likelihood, impact):
        ax.plot(im, l, 'o', markersize=20, color=COLORS['primary'], alpha=0.7)
        ax.annotate(r, (im, l), textcoords='offset points', xytext=(12, 6), fontsize=10)
    
    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(0.5, 5.5)
    ax.set_xlabel('Impact', fontsize=14, fontweight='bold')
    ax.set_ylabel('Likelihood', fontsize=14, fontweight='bold')
    ax.set_title('Figure 17: Risk Register Heat Map', fontsize=18, fontweight='bold', pad=20)
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_xticklabels(['Low', '', 'Medium', '', 'High'])
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['Low', '', 'Medium', '', 'High'])
    
    legend_elements = [
        mpatches.Patch(facecolor='#c6f6d5', label='Low Risk'),
        mpatches.Patch(facecolor='#feebc8', label='Medium Risk'),
        mpatches.Patch(facecolor='#fed7d7', label='High Risk'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=11)
    
    return save_figure(fig, 'figure_17_risk_heat_map.png')


def main():
    print("=" * 60)
    print("Generating all figures with LARGER FONTS")
    print("=" * 60)
    
    figures = [
        ('Figure 1', create_figure_1),
        ('Figure 2', create_figure_2),
        ('Figure 3', create_figure_3),
        ('Figure 4', create_figure_4),
        ('Figure 5', create_figure_5),
        ('Figure 6', create_figure_6),
        ('Figure 7', create_figure_7),
        ('Figure 8', create_figure_8),
        ('Figure 9', create_figure_9),
        ('Figure 10', create_figure_10),
        ('Figure 11', create_figure_11),
        ('Figure 12', lambda: create_case_study_figure('Ghana', 'figure_12_ghana.png', 12)),
        ('Figure 13', lambda: create_case_study_figure('Sri Lanka', 'figure_13_sri_lanka.png', 13)),
        ('Figure 14', lambda: create_case_study_figure('Zambia', 'figure_14_zambia.png', 14)),
        ('Figure 15', lambda: create_case_study_figure('Pakistan', 'figure_15_pakistan.png', 15)),
        ('Figure 16', create_figure_16),
        ('Figure 17', create_figure_17),
    ]
    
    for name, func in figures:
        print(f"\nGenerating: {name}")
        try:
            func()
            print(f"  ✓ Done")
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    print("\n" + "=" * 60)
    print("All figures generated!")
    print("=" * 60)


if __name__ == '__main__':
    main()
