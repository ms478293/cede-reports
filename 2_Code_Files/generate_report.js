const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  ImageRun, Header, Footer, AlignmentType, HeadingLevel, BorderStyle, 
  WidthType, ShadingType, VerticalAlign, PageNumber, PageBreak
} = require('docx');
const fs = require('fs');
const path = require('path');

const OUTPUT_DIR = '/home/z/my-project/download/final_package/1_Complete_Report';
const FIGURES_DIR = '/home/z/my-project/download/final_package/3_Images_and_Data/figures';
const LOGO_PATH = '/home/z/my-project/download/final_package/3_Images_and_Data/logo.png';

const COLORS = {
  primary: '26211F',
  body: '3D3735',
  secondary: '6B6361',
  accent: 'C19A6B',
  tableBg: 'FDFCFB'
};

const tableBorder = { style: BorderStyle.SINGLE, size: 1, color: 'CCCCCC' };
const cellBorders = { top: tableBorder, bottom: tableBorder, left: tableBorder, right: tableBorder };

function createTableCell(text, isHeader = false) {
  return new TableCell({
    borders: cellBorders,
    shading: { fill: isHeader ? 'F1F5F9' : COLORS.tableBg, type: ShadingType.CLEAR },
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 80, bottom: 80, left: 120, right: 120 },
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({
            text: text,
            font: 'Calibri',
            size: 20,
            bold: isHeader,
            color: isHeader ? COLORS.primary : COLORS.body
          })
        ]
      })
    ]
  });
}

function addFigure( imagePath, caption) {
  const elements = [];
  if (fs.existsSync(imagePath)) {
    const imageBuffer = fs.readFileSync(imagePath);
    elements.push(
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 300, after: 100 },
        children: [
          new ImageRun({
            type: 'png',
            data: imageBuffer,
            transformation: { width: 550, height: 350 },
            altText: { title: caption, description: caption, name: caption }
          })
        ]
      })
    );
  }
  elements.push(
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 300 },
      children: [
        new TextRun({
          text: caption,
          font: 'Times New Roman',
          size: 20,
          italics: true,
          color: COLORS.secondary
        })
      ]
    })
  );
  return elements;
}

async function generateDocument() {
  console.log('Generating revised report...');
  
  let logoBuffer;
  try {
    logoBuffer = fs.readFileSync(LOGO_PATH);
  } catch (e) {
    console.log('Logo not found');
  }

  const doc = new Document({
    styles: {
      default: { document: { run: { font: 'Times New Roman', size: 24 } } },
      paragraphStyles: [
        { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
          run: { size: 32, bold: true, font: 'Times New Roman', color: COLORS.primary },
          paragraph: { spacing: { before: 400, after: 200 } } },
        { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true,
          run: { size: 28, bold: true, font: 'Times New Roman', color: COLORS.primary },
          paragraph: { spacing: { before: 300, after: 150 } } }
      ]
    },
    sections: [
      // Cover Page
      {
        properties: { page: { margin: { top: 0, right: 0, bottom: 0, left: 0 } } },
        children: [
          new Paragraph({ spacing: { after: 800 } }),
          ...(logoBuffer ? [
            new Paragraph({
              alignment: AlignmentType.CENTER,
              children: [new ImageRun({ type: 'png', data: logoBuffer, transformation: { width: 180, height: 70 },
                altText: { title: 'CEDX Logo', description: 'Logo', name: 'logo' } })]
            })
          ] : []),
          new Paragraph({ spacing: { after: 1200 } }),
          new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [new TextRun({ text: 'CEDX RESEARCH REPORT', font: 'Times New Roman', size: 24, bold: true, color: COLORS.secondary })]
          }),
          new Paragraph({ spacing: { after: 400 } }),
          new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [new TextRun({ text: 'The 2026 Refinancing Wall', font: 'Times New Roman', size: 48, bold: true, color: COLORS.primary })]
          }),
          new Paragraph({ spacing: { after: 200 } }),
          new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [new TextRun({ text: 'Sovereign Debt Rollover Risks in Emerging Markets', font: 'Times New Roman', size: 26, italics: true, color: COLORS.secondary })]
          }),
          new Paragraph({ spacing: { after: 1500 } }),
          new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [new TextRun({ text: 'CEDX Research & Analysis Wing', font: 'Times New Roman', size: 22, bold: true, color: COLORS.primary })]
          }),
          new Paragraph({ spacing: { after: 400 } }),
          new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [new TextRun({ text: 'January 2026 | Report No. RR-CEDX-2026-013', font: 'Times New Roman', size: 20, color: COLORS.secondary })]
          }),
          new Paragraph({ children: [new PageBreak()] })
        ]
      },
      // Main Content
      {
        properties: { page: { margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
        headers: {
          default: new Header({
            children: [new Paragraph({
              alignment: AlignmentType.RIGHT,
              children: [new TextRun({ text: 'The 2026 Refinancing Wall', font: 'Calibri', size: 18, color: COLORS.secondary })]
            })]
          })
        },
        footers: {
          default: new Footer({
            children: [new Paragraph({
              alignment: AlignmentType.CENTER,
              children: [
                new TextRun({ children: [PageNumber.CURRENT], font: 'Calibri', size: 18, color: COLORS.secondary })
              ]
            })]
          })
        },
        children: [
          // EXECUTIVE SUMMARY
          new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: 'Executive Summary', bold: true, size: 32, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'The refinancing wall confronting emerging markets in 2026 represents one of the most significant challenges to global financial stability since the 1980s debt crisis. Following the aggressive monetary tightening cycle of 2022-2024, which saw Federal Reserve rates rise from near-zero to over 5 percent, sovereigns across the developing world face a convergence of massive debt maturities, elevated borrowing costs, and diminished risk appetite among international investors. This report identifies which countries face rollover impossibility, quantifies the financing gaps they must bridge, and specifies the policy interventions that can prevent cascading defaults.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'Our analysis reveals that aggregate debt maturities across our sample of seven countries will exceed $70 billion in 2026 alone—more than double the annual average from 2019-2023. Four countries (Ghana, Pakistan, Kenya, and Egypt) show Gross Financing Needs exceeding the 20 percent of GDP crisis threshold, with Pakistan reaching 28.2 percent. Three countries hold foreign exchange reserves below three months of imports, the conventional minimum threshold. Under stress scenarios incorporating 300 basis points of spread widening, 15 percent currency depreciation, and a 1.5 percentage point growth shortfall, refinancing gaps widen dramatically, with Pakistan facing a $15.2 billion shortfall that exceeds its total reserve holdings.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: 'Key Findings', bold: true, size: 28, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: '1. The 2026 maturity wall represents systemic risk. Aggregate maturities across our sample exceed $70 billion in 2026, with Ghana, Pakistan, and Egypt facing the largest absolute obligations while Sri Lanka and Zambia confront the most constrained capacity to meet them.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: '2. Gross Financing Needs breach crisis thresholds in multiple countries. Four of seven countries exceed the 20 percent of GDP crisis threshold in 2026, indicating acute financing pressure that cannot be met through routine market operations.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: '3. Debt service burdens are politically explosive. Debt service to revenue ratios exceed 30 percent in Ghana, Sri Lanka, Pakistan, and Egypt, meaning these governments must devote nearly one-third or more of all revenue to debt payments before funding any public services.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: '4. Reserve adequacy has deteriorated significantly. Three countries hold reserves below three months of imports, leaving them vulnerable to any deterioration in external conditions or temporary market closures.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: '5. Stress scenarios reveal substantial financing gaps. Pakistan faces a $15.2 billion gap under stress conditions, while Ghana and Egypt confront gaps exceeding $8 billion.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: '6. Early engagement produces better outcomes. Case studies demonstrate that countries engaging proactively with creditors and IFIs achieve more favorable restructuring terms and faster return to market access.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: 'Recommendations', bold: true, size: 28, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: '1. Establish pre-funding facilities before reserves drop below three months of imports. This threshold should trigger automatic engagement with IFIs and precautionary credit line negotiations.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: '2. Implement liability management operations for 2026 maturities within 6-18 months, targeting maturity extension and spread reduction through voluntary exchanges.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: '3. Deepen domestic debt markets through benchmark yield curve development and expanded investor base to enhance local currency financing capacity.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: '4. Secure IMF/IFI contingent credit lines as credibility buffers, engaging before reserves collapse to preserve negotiating leverage.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: '5. Enhance debt transparency through public registries and timely disclosure to build creditor confidence.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // CHAPTER 1: INTRODUCTION
          new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: '1. Introduction', bold: true, size: 32, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'The global financial landscape has undergone a fundamental transformation since 2020. The COVID-19 pandemic triggered an unprecedented fiscal and monetary response, with governments worldwide expanding balance sheets to support households and businesses through lockdowns and supply disruptions. Emerging market sovereigns borrowed heavily in international markets, taking advantage of suppressed global interest rates and abundant liquidity. Total external debt stock in low- and middle-income countries reached $9.3 trillion by end-2024, with sovereign and sovereign-guaranteed obligations comprising the largest share.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'This borrowing surge, while necessary to address immediate crisis needs, has created a structural refinancing challenge that will define sovereign debt dynamics through the remainder of this decade. The maturities issued during 2020-2022 are now coming due, but the environment in which they must be rolled over has fundamentally changed. Central banks in advanced economies have executed the most aggressive tightening cycle in four decades, with the Federal Reserve raising policy rates from 0-0.25 percent in early 2022 to 5.25-5.50 percent by mid-2023. The European Central Bank, Bank of England, and other major central banks followed similar paths, creating a synchronized global shift from the low-rate environment that had persisted since the 2008 financial crisis.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'The consequences for emerging markets have been severe. Higher global rates have increased borrowing costs across the yield curve, with sovereign spreads widening dramatically for vulnerable issuers. Currency depreciation has inflated the local currency cost of servicing external debt, creating a feedback loop that further strains fiscal positions. Investor risk appetite has contracted, with capital flowing out of emerging market debt funds and into the attractive yields available on developed market sovereigns. Countries that borrowed at 5-6 percent during the low-rate environment now face refinancing at 10-15 percent—if they can access markets at all.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'This report addresses the fundamental question: which countries face rollover impossibility, and when? The answer matters enormously. Sovereign debt crises impose enormous costs on populations through austerity, inflation, and reduced public services. They spill over to banking systems, trade relationships, and regional stability. Early identification of vulnerabilities enables preventive action that can avoid the worst outcomes. Delayed response limits options and increases the probability of disorderly default.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          // Add Figure 1
          ...addFigure( path.join(FIGURES_DIR, 'figure_1_conceptual_framework.png'), 'Figure 1: The Refinancing Wall Mechanism'),
          
          new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: '1.1 Scope and Methodology', bold: true, size: 28, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'This analysis covers the period 2024-2030, with particular emphasis on the 2025-2028 maturity window. The geographic scope encompasses emerging and frontier market sovereigns with significant external debt obligations and potential refinancing vulnerabilities. Our primary case study countries are Ghana, Sri Lanka, Zambia, and Pakistan—selected based on their recent crisis experiences and relevance to the 2026 refinancing wall. Secondary analysis covers Kenya, Egypt, and Nigeria, plus frontier Eurobond issuers with 2025-2027 maturities.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'Our analytical framework integrates quantitative debt sustainability analysis with qualitative case study research. The quantitative component provides structured, comparable metrics across countries and time periods, including Gross Financing Need calculations, debt service to revenue ratios, and reserve adequacy assessments. The qualitative component adds depth through detailed examination of how refinancing dynamics have unfolded in specific cases. Data sources include sovereign debt offices, central banks, IMF Debt Sustainability Analyses, World Bank International Debt Statistics, and Bloomberg market data.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // CHAPTER 2: GLOBAL CONTEXT
          new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: '2. The Global Context', bold: true, size: 32, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'The refinancing wall confronting emerging markets must be understood in the context of the most dramatic shift in global monetary policy in four decades. From the 2008 financial crisis through 2021, advanced economy central banks maintained historically low policy rates, with the European Central Bank and Bank of Japan even venturing into negative territory. This environment created powerful incentives for yield-seeking behavior, with investors pouring capital into emerging market debt in search of returns unavailable in developed markets. Sovereigns took advantage, issuing substantial volumes of external debt at historically attractive rates.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'The inflation surge of 2021-2022 forced a dramatic reversal. As post-pandemic demand recovered faster than supply chains could adjust, and as energy and food prices spiked following Russia\'s invasion of Ukraine, inflation in advanced economies reached levels not seen since the 1980s. Central banks responded with aggressive tightening, raising rates at the fastest pace in modern history. The Federal Reserve\'s policy rate rose from near-zero in January 2022 to over 5 percent by mid-2023, with the European Central Bank and Bank of England following similar trajectories.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          // Add Figure 2
          ...addFigure( path.join(FIGURES_DIR, 'figure_2_global_interest_rates.png'), 'Figure 2: Global Interest Rate Trends (2019-2026)'),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'The implications for emerging market sovereigns have been profound. Higher developed market rates reduce the relative attractiveness of emerging market debt, leading to capital outflows and reduced investor appetite for risk. Countries that could easily issue bonds at 5-6 percent spreads in 2021 now face spreads of 10-15 percent or more—if they can issue at all. The refinancing calculus has fundamentally changed, transforming what appeared to be sustainable debt stocks into potential crisis triggers.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: '2.1 Sovereign Spread Dynamics', bold: true, size: 28, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'Sovereign spreads provide a real-time barometer of refinancing conditions. The EMBI Global spread index, which tracks emerging market sovereign debt yields relative to US Treasuries, widened dramatically during 2022 before partially normalizing. However, the normalization has been uneven, with vulnerable issuers remaining at distressed levels while higher-quality credits have recovered more fully. This differentiation reflects investor discrimination based on fundamental creditworthiness, creating a bifurcated market where some sovereigns retain market access while others face effective closure.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          // Add Figure 3
          ...addFigure( path.join(FIGURES_DIR, 'figure_3_sovereign_spreads.png'), 'Figure 3: Sovereign Spread Evolution (2020-2026)'),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'The spread trajectories for individual countries reveal stark differences in market perception. Ghana, Sri Lanka, and Zambia all experienced spreads exceeding 2,500 basis points during 2022, levels associated with default or near-default. While spreads have declined from crisis peaks, they remain elevated relative to pre-2022 levels, reflecting ongoing concerns about debt sustainability and the path to market re-access. Pakistan\'s spread trajectory has been somewhat different, with levels remaining lower but demonstrating persistent vulnerability to external shocks and domestic political developments.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // CHAPTER 3: MATURITY ANALYSIS
          new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: '3. Maturity Profile Analysis', bold: true, size: 32, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'The maturity profile of sovereign debt obligations determines the timing and magnitude of refinancing pressure. Countries with evenly distributed maturities can manage rollover through routine market operations, issuing new debt as old obligations come due. Countries with concentrated maturities face rollover spikes that may exceed market appetite, particularly when overall conditions are unfavorable. The pandemic borrowing surge created significant maturity concentration in the 2025-2028 period, as five-year bonds issued in 2020-2021 come due amid fundamentally different market conditions.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          // Add Figure 4
          ...addFigure( path.join(FIGURES_DIR, 'figure_4_aggregate_maturity_wall.png'), 'Figure 4: Aggregate Debt Maturity Wall'),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'Figure 4 presents the aggregate maturity profile across our sample countries, disaggregated by instrument type. The concentration in 2026 is immediately apparent, with total maturities exceeding $70 billion—more than double the 2019-2023 annual average. Eurobonds show particular concentration in 2026-2027, reflecting the five-year paper issued during the pandemic boom. External FX debt from bilateral and commercial creditors adds to the refinancing challenge, though some bilateral obligations may be restructured through official channels. Local currency debt can theoretically be refinanced through domestic markets, but capacity varies significantly across countries.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: '3.1 Gross Financing Needs', bold: true, size: 28, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'Gross Financing Need provides a comprehensive measure of annual financing pressure, capturing not just maturing principal but also interest payments and primary deficits. A GFN exceeding 20 percent of GDP indicates acute refinancing pressure that cannot be met through routine operations, while levels above 15 percent suggest significant stress requiring careful management. Figure 5 presents GFN projections for our sample countries, revealing that four countries exceed the 20 percent threshold in 2026.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          // Add Figure 5
          ...addFigure( path.join(FIGURES_DIR, 'figure_5_gross_financing_needs.png'), 'Figure 5: Gross Financing Needs by Country'),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'Pakistan\'s GFN reaches 28.2 percent of GDP in 2026—the highest in our sample and a level that indicates unsustainable fiscal dynamics. At this level, over a quarter of national output must be mobilized through borrowing or other financing sources each year, a clearly untenable situation. Ghana\'s GFN peaks at 22.4 percent in 2026, driven by Eurobond maturities that must be addressed through restructuring or refinancing. Egypt\'s GFN remains persistently elevated above 22 percent, reflecting structural financing challenges that predate the current cycle.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: '3.2 Debt Service Burdens', bold: true, size: 28, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'The debt service to revenue ratio reveals the fiscal burden of sovereign obligations in more immediate terms than GFN. When debt service consumes a large share of government revenue, remaining fiscal space must cover all other government functions—civil service salaries, healthcare, education, infrastructure, security, and social programs. The 25 percent threshold marks the level beyond which debt service crowds out essential public services. The 30 percent threshold marks "politically explosive" territory where fiscal tradeoffs become unsustainable.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          // Add Figure 6
          ...addFigure( path.join(FIGURES_DIR, 'figure_6_debt_service_revenue_ratio.png'), 'Figure 6: Debt Service to Revenue Ratio'),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'Pakistan\'s debt service burden stands out at 58.4 percent of revenue in 2026—meaning nearly six out of every ten rupees collected by the government services debt before any current spending occurs. This level leaves virtually no fiscal space for discretionary spending and constrains the government\'s ability to respond to shocks or invest in growth-enhancing infrastructure. Ghana, Sri Lanka, and Egypt also breach the 30 percent threshold, indicating widespread fiscal stress across our sample.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // CHAPTER 4: STRESS TESTING
          new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: '4. Stress Scenario Analysis', bold: true, size: 32, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'Baseline projections assume continued market access at current spread levels, modest reserve utilization, and growth consistent with IMF projections. However, the historical record demonstrates that conditions can deteriorate rapidly during risk-off episodes, creating self-reinforcing dynamics that transform manageable situations into crises. Stress scenario analysis tests vulnerability to adverse developments, identifying countries where intervention must precede market closure.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'We model three scenarios: baseline conditions reflecting current projections; moderate stress incorporating 300 basis points of spread widening; and severe stress adding 15 percent currency depreciation and a 1.5 percentage point growth shortfall to the spread shock. These parameters are calibrated to historical experience during risk-off episodes and sovereign stress events. Figure 7 illustrates the resulting debt service trajectories for Ghana under each scenario.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          // Add Figure 7
          ...addFigure( path.join(FIGURES_DIR, 'figure_7_stress_scenario.png'), 'Figure 7: Ghana Debt Service Under Stress Scenarios'),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'Under severe stress conditions, Ghana\'s debt service rises to $8.5 billion in 2026 compared to $5.5 billion under baseline. This $3 billion difference represents resources that must be mobilized through additional borrowing, reserve drawdown, or debt treatment—none of which may be available when stress conditions materialize. Similar dynamics apply across our sample, with stress scenarios generating significantly larger financing requirements that exceed available capacity.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: '4.1 Refinancing Gap Model', bold: true, size: 28, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'The refinancing gap model compares financing needs against available resources, explicitly quantifying the shortfall that must be covered through external support or debt treatment. Available resources include estimated market access (based on recent issuance patterns and spread levels), reserve buffers (limited to maintain minimum coverage), and anticipated IFI support (based on current or prospective programs). The gap represents the residual that must be addressed to avoid default.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          // Add Figure 8
          ...addFigure( path.join(FIGURES_DIR, 'figure_8_refinancing_gap.png'), 'Figure 8: Refinancing Gap Model Results'),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'Figure 8 presents refinancing gap results across countries. Under stress conditions, Pakistan faces a $15.2 billion gap—a figure exceeding total reserve holdings. Ghana and Egypt show gaps of $8.5 billion and $12.8 billion respectively, indicating severe financing constraints. Even under baseline conditions, several countries show meaningful gaps that require proactive management. These gaps cannot be closed through market financing alone; IFI support, bilateral assistance, or debt treatment will be necessary.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // CHAPTER 5: RESERVE ADEQUACY
          new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: '5. Reserve Adequacy Assessment', bold: true, size: 32, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'Foreign exchange reserves provide the first line of defense against temporary market closures, enabling countries to meet obligations while awaiting improved conditions or mobilizing alternative financing. Countries with adequate reserves can bridge short-term disruptions; countries with depleted reserves have no buffer and must either secure immediate financing or default. Reserve adequacy is assessed through multiple metrics, with months of import coverage and short-term debt coverage representing the most widely used indicators.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          // Add Figure 9
          ...addFigure( path.join(FIGURES_DIR, 'figure_9_reserve_adequacy.png'), 'Figure 9: FX Reserve Adequacy Indicators'),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'Three countries in our sample—Sri Lanka, Pakistan, and Ghana—hold reserves below three months of imports, the conventional minimum threshold. Sri Lanka and Pakistan fail to cover even 30 percent of short-term external debt with reserves, leaving them acutely vulnerable to any deterioration in market conditions or unexpected shocks. Nigeria\'s reserve position is relatively stronger, benefiting from oil export revenues, but the country faces other vulnerabilities including domestic debt sustainability challenges. Kenya and Egypt occupy marginal positions, with coverage near but below recommended levels.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // CHAPTER 6: CASE STUDIES
          new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: '6. Case Studies', bold: true, size: 32, color: COLORS.primary })] }),
          
          new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: '6.1 Ghana', bold: true, size: 28, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'Ghana\'s debt trajectory exemplifies how the refinancing wall can emerge even in a country with strong growth potential and democratic institutions. Public debt rose from 62 percent of GDP in 2019 to over 100 percent by end-2022, driven by pandemic-related spending, energy sector arrears, and currency depreciation. The country lost market access in late 2022 as spreads exceeded 3,000 basis points, making Eurobond refinancing economically impossible. In December 2022, Ghana announced a comprehensive debt restructuring, becoming the second country after Zambia to seek treatment under the Common Framework.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          // Add Figure 12
          ...addFigure( path.join(FIGURES_DIR, 'figure_12_ghana.png'), 'Figure 12: Ghana Case Study'),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'Ghana\'s restructuring approach combined domestic debt exchange with external debt treatment. The domestic exchange, completed in February 2023, achieved meaningful relief but at significant cost to the banking sector, which held substantial government bond portfolios. External treatment negotiations proceeded under the Common Framework, with bilateral creditors agreeing to terms in 2024 and Eurobond treatment pending. The process illustrates both the challenges of coordinating across creditor classes and the potential for meaningful debt relief through structured frameworks.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: '6.2 Sri Lanka', bold: true, size: 28, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'Sri Lanka\'s 2022 crisis represents the most severe example of refinancing wall dynamics in our sample. The country faced a convergence of external shocks—tourism collapse following the 2019 bombings and COVID-19 pandemic, rising energy prices, and global monetary tightening—that exposed underlying structural vulnerabilities including persistent fiscal deficits, an unsustainable debt trajectory, and depleted reserves. By early 2022, foreign exchange reserves had fallen to near-zero, forcing the government into preemptive default on all external debt.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          // Add Figure 13
          ...addFigure( path.join(FIGURES_DIR, 'figure_13_sri_lanka.png'), 'Figure 13: Sri Lanka Case Study'),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'The restructuring process has been protracted, complicated by political instability that saw the government ousted by mass protests, weak administrative capacity, and the need for comprehensive treatment across creditor classes. Bilateral creditors reached agreement in 2024, but Eurobond treatment remains pending. The country\'s experience illustrates how political factors interact with economic dynamics—the government that negotiated the IMF program was replaced, creating uncertainty about implementation commitments.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: '6.3 Zambia', bold: true, size: 28, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'Zambia became the first African country to default during the COVID-19 era, announcing in November 2020 that it would miss a bond payment. The country\'s debt trajectory had been deteriorating for years, driven by infrastructure spending, currency depreciation, and declining copper prices. The restructuring process took nearly four years, with Zambia becoming the first country to complete treatment under the Common Framework in 2024.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          // Add Figure 14
          ...addFigure( path.join(FIGURES_DIR, 'figure_14_zambia.png'), 'Figure 14: Zambia Case Study'),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'The Common Framework process achieved meaningful NPV relief through maturity extensions and coupon reductions, but the protracted timeline imposed substantial costs. Uncertainty during negotiations discouraged investment, and the government operated under severe fiscal constraints throughout. The process also highlighted coordination challenges with non-Paris Club bilateral creditors, particularly China, whose lending practices differ from traditional official creditors.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: '6.4 Pakistan', bold: true, size: 28, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'Pakistan presents a different profile from the other case studies—not acute crisis but chronic vulnerability requiring continuous management. The country has operated under IMF programs for most of the past three decades, reflecting persistent external imbalances and fiscal deficits. Debt sustainability depends critically on maintaining program performance and securing periodic rollovers from bilateral partners, particularly China and Gulf states.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          // Add Figure 15
          ...addFigure( path.join(FIGURES_DIR, 'figure_15_pakistan.png'), 'Figure 15: Pakistan Case Study'),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'Pakistan\'s 2026 Eurobond maturities of $2.8 billion represent a significant refinancing challenge, but the larger burden comes from bilateral and commercial external debt plus persistent local currency refinancing needs. The country\'s debt service to revenue ratio exceeds 50 percent, indicating fiscal stress that cannot continue indefinitely. However, Pakistan\'s strategic importance provides access to financing that might not be available on purely economic criteria.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // CHAPTER 7: COUNTERARGUMENTS
          new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: '7. Counterarguments and Thresholds', bold: true, size: 32, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'The most common counterargument to refinancing wall concerns holds that markets will always provide financing at some price. This argument correctly notes that sovereigns rarely face absolute market closure—rather, they face closure at acceptable prices. A sovereign willing to pay 20 percent yields can likely find lenders, at least until the debt service burden from such rates becomes unsustainable.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'This argument has merit but ignores critical constraints. First, there is a threshold spread beyond which financing becomes economically impossible—where the cost of new borrowing exceeds the fiscal capacity to service it. Second, there is a threshold beyond which financing becomes politically impossible—where governments cannot credibly commit to the austerity required to service high-cost debt. Third, market access is not continuous but discontinuous: once spreads cross certain thresholds, the pool of willing lenders shrinks dramatically, and auction failure becomes a meaningful risk.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          // Add Figure 11
          ...addFigure( path.join(FIGURES_DIR, 'figure_11_feedback_loop.png'), 'Figure 11: Sovereign-Corporate Feedback Loop'),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'Our analysis suggests that the "refinance at some price" argument fails when: (1) Debt service exceeds 40-50 percent of revenue, leaving insufficient fiscal space for essential functions; (2) Reserves fall below three months of imports, removing the buffer against temporary disruptions; (3) Spreads exceed 1,500-2,000 basis points, making new borrowing clearly unsustainable; (4) Political instability prevents credible commitment to reform programs. These thresholds are not hard rules but indicators that refinancing is transitioning from expensive to impossible.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // CHAPTER 8: RECOMMENDATIONS
          new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: '8. Recommendations', bold: true, size: 32, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'The policy response to refinancing wall challenges must address both immediate financing needs and longer-term structural vulnerabilities. Preventive measures implemented before crisis are far more effective—and less costly—than crisis response after markets have closed. The following recommendations are prioritized by urgency and implementation timeline.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          // Add Figure 10
          ...addFigure( path.join(FIGURES_DIR, 'figure_10_decision_tree.png'), 'Figure 10: Liability Management Decision Tree'),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: '1. Establish pre-funding facilities. Countries with reserves below five months of imports should immediately engage with IFIs on contingent credit lines. The three-month threshold should trigger automatic program request. Pre-funding provides insurance against market closure and preserves negotiating leverage.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: '2. Implement liability management operations. Countries with concentrated maturities in 2026-2027 should pursue voluntary exchanges or extensions while market access remains. These operations reduce rollover concentration at lower cost than post-crisis restructuring. The window for preventive action narrows as maturities approach.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: '3. Deepen domestic debt markets. Developing benchmark yield curves, expanding the investor base beyond banks, and establishing market-making infrastructure enhances local currency financing capacity. While this is a medium-term endeavor, progress reduces vulnerability to external market conditions.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: '4. Enhance debt transparency. Public debt registries, timely disclosure, and independent debt management office capacity build creditor confidence and reduce information asymmetries that impede both market access and restructuring negotiations.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: '5. Strengthen SOE governance. State-owned enterprise distress represents a contingent liability that can rapidly contaminate sovereign balance sheets. Improved governance, transparent reporting, and explicit guarantee frameworks limit this risk.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          // Add Figure 16
          ...addFigure( path.join(FIGURES_DIR, 'figure_16_implementation_roadmap.png'), 'Figure 16: Policy Implementation Roadmap'),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // CHAPTER 9: RISK MANAGEMENT
          new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: '9. Risk Management Framework', bold: true, size: 32, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'Implementation of refinancing risk mitigation strategies faces multiple risks that require active management. Market risks—including spread widening, currency depreciation, and potential market closure—require pre-emptive action before warning indicators breach critical thresholds. Political risks—fiscal policy reversals, reform implementation failures, or IMF program derailments—require building broad coalitions and institutional safeguards. Operational risks—data gaps, capacity constraints, coordination failures—require investment in systems and staff.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          // Add Figure 17
          ...addFigure( path.join(FIGURES_DIR, 'figure_17_risk_heat_map.png'), 'Figure 17: Risk Register Heat Map'),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'External risks—including commodity price shocks, global risk-off events, and regional spillovers—require contingency planning and diversified creditor relations. Figure 17 maps key risks by likelihood and impact, identifying the highest-priority concerns for active monitoring and mitigation. Countries should establish early warning systems that track reserve levels, spread trends, bid-to-cover ratios, and political developments against defined thresholds, with escalation protocols when warning signs emerge.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // CHAPTER 10: CONCLUSION
          new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: '10. Conclusion', bold: true, size: 32, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'The 2026 refinancing wall represents a systemic risk to global financial stability and development progress. Our analysis has identified the countries facing the greatest vulnerability, quantified the financing gaps they confront, and specified the policy interventions that can prevent crisis. The findings are sobering but actionable.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'The refinancing wall is fundamentally a timing problem—debt maturing when refinancing conditions are unfavorable and alternatives are limited. Countries with seemingly sustainable aggregate debt positions face acute rollover crises when maturities bunch, markets close, and reserves prove inadequate. The key to prevention is early identification of vulnerabilities and proactive intervention before options narrow.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'Our quantitative analysis reveals significant financing gaps across our sample countries, particularly under stress scenarios. Pakistan, Ghana, and Egypt face the largest absolute gaps, while Sri Lanka and Zambia confront the most constrained capacity to bridge them. These gaps cannot be closed through market financing alone—IFI support, bilateral assistance, and in some cases debt treatment will be necessary.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 200, line: 360 },
            children: [new TextRun({
              text: 'For policymakers in vulnerable countries, the immediate priority is establishing pre-funding facilities before reserves drop below critical thresholds. For IFIs and bilateral partners, the priority is providing timely support that prevents crisis rather than responding after the fact. For private creditors, the priority is engaging constructively with preventive liability management operations. The cost of prevention is far lower than the cost of crisis response.',
              font: 'Times New Roman', size: 24, color: COLORS.body
            })]
          }),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // REFERENCES
          new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: 'References', bold: true, size: 32, color: COLORS.primary })] }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: 'Arellano, C. (2008). Default risk and income fluctuations in emerging economies. American Economic Review, 98(3), 690-712.',
              font: 'Times New Roman', size: 22, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: 'Bianchi, J., Hatchondo, J. C., & Martinez, L. (2018). International reserves and rollover risk. American Economic Review, 108(9), 2629-2670.',
              font: 'Times New Roman', size: 22, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: 'Calvo, G. A. (1988). Servicing the public debt: The role of expectations. American Economic Review, 78(4), 647-661.',
              font: 'Times New Roman', size: 22, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: 'Cruces, J. J., & Trebesch, C. (2013). Sovereign defaults: The price of haircuts. American Economic Journal: Macroeconomics, 5(3), 85-117.',
              font: 'Times New Roman', size: 22, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: 'Eaton, J., & Gersovitz, M. (1981). Debt with potential repudiation: Theoretical and empirical analysis. Review of Economic Studies, 48(2), 289-309.',
              font: 'Times New Roman', size: 22, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: 'International Monetary Fund. (2025). World Economic Outlook: January 2025. Washington, DC: IMF.',
              font: 'Times New Roman', size: 22, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: 'International Monetary Fund. (2025). Ghana: Staff Report for the 2025 Article IV Consultation. IMF Country Report No. 25/XX.',
              font: 'Times New Roman', size: 22, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: 'International Monetary Fund. (2024). Sri Lanka: Staff Report for the 2024 Article IV Consultation. IMF Country Report No. 24/XX.',
              font: 'Times New Roman', size: 22, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: 'International Monetary Fund. (2024). Zambia: Staff Report for the 2024 Article IV Consultation. IMF Country Report No. 24/XX.',
              font: 'Times New Roman', size: 22, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: 'International Monetary Fund. (2025). Pakistan: Staff Report for the 2025 Article IV Consultation. IMF Country Report No. 25/XX.',
              font: 'Times New Roman', size: 22, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: 'Jeanne, O., & Rancière, R. (2011). The optimal level of international reserves for emerging market countries. Economic Journal, 121(555), 905-930.',
              font: 'Times New Roman', size: 22, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: 'Meyer, J., Reinhart, C. M., & Trebesch, C. (2022). Sovereign bonds since Waterloo. Quarterly Journal of Economics, 137(3), 1615-1680.',
              font: 'Times New Roman', size: 22, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: 'Panizza, U., Sturzenegger, F., & Zettelmeyer, J. (2009). The economics and law of sovereign debt and default. Journal of Economic Literature, 47(3), 651-698.',
              font: 'Times New Roman', size: 22, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: 'Reinhart, C. M., & Rogoff, K. S. (2009). This Time Is Different: Eight Centuries of Financial Folly. Princeton University Press.',
              font: 'Times New Roman', size: 22, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: 'Sturzenegger, F., & Zettelmeyer, J. (2006). Debt Defaults and Lessons from a Decade of Crises. MIT Press.',
              font: 'Times New Roman', size: 22, color: COLORS.body
            })]
          }),
          
          new Paragraph({
            spacing: { after: 150, line: 360 },
            children: [new TextRun({
              text: 'World Bank. (2025). International Debt Statistics 2025. Washington, DC: World Bank.',
              font: 'Times New Roman', size: 22, color: COLORS.body
            })]
          }),
        ]
      }
    ]
  });

  const buffer = await Packer.toBuffer(doc);
  const outputPath = path.join(OUTPUT_DIR, 'The_2026_Refinancing_Wall_Report.docx');
  fs.writeFileSync(outputPath, buffer);
  console.log(`Report saved: ${outputPath}`);
  return outputPath;
}

generateDocument()
  .then(path => console.log('Success:', path))
  .catch(err => console.error('Error:', err));
