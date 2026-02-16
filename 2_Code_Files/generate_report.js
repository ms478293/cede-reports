const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  ImageRun, Header, Footer, AlignmentType, PageOrientation, LevelFormat,
  TableOfContents, HeadingLevel, BorderStyle, WidthType, ShadingType,
  VerticalAlign, PageNumber, PageBreak
} = require('docx');
const fs = require('fs');
const path = require('path');

// Configuration
const OUTPUT_DIR = '/home/z/my-project/download/refinancing_wall_report';
const FIGURES_DIR = path.join(OUTPUT_DIR, 'figures');
const LOGO_PATH = path.join(OUTPUT_DIR, 'logo.png');

// Color Palette - Terra Cotta Afterglow
const COLORS = {
  primary: '26211F',
  body: '3D3735',
  secondary: '6B6361',
  accent: 'C19A6B',
  tableBg: 'FDFCFB',
  white: 'FFFFFF',
  lightGray: 'F1F5F9'
};

// Helper functions
const createParagraph = (text, options = {}) => {
  return new Paragraph({
    alignment: options.alignment || AlignmentType.LEFT,
    spacing: { after: 200, line: 312 },
    children: [
      new TextRun({
        text: text,
        font: 'Times New Roman',
        size: options.size || 22,
        bold: options.bold || false,
        color: options.color || COLORS.body
      })
    ]
  });
};

const createHeading1 = (text) => {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 400, after: 200 },
    children: [
      new TextRun({
        text: text,
        font: 'Times New Roman',
        size: 32,
        bold: true,
        color: COLORS.primary
      })
    ]
  });
};

const createHeading2 = (text) => {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 300, after: 150 },
    children: [
      new TextRun({
        text: text,
        font: 'Times New Roman',
        size: 28,
        bold: true,
        color: COLORS.primary
      })
    ]
  });
};

const createHeading3 = (text) => {
  return new Paragraph({
    heading: HeadingLevel.HEADING_3,
    spacing: { before: 200, after: 100 },
    children: [
      new TextRun({
        text: text,
        font: 'Times New Roman',
        size: 24,
        bold: true,
        color: COLORS.secondary
      })
    ]
  });
};

const createFigure = (imagePath, caption, source) => {
  const elements = [];
  
  if (fs.existsSync(imagePath)) {
    const imageBuffer = fs.readFileSync(imagePath);
    elements.push(
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 200, after: 100 },
        children: [
          new ImageRun({
            type: 'png',
            data: imageBuffer,
            transformation: { width: 500, height: 300 },
            altText: { title: caption, description: caption, name: caption }
          })
        ]
      })
    );
  }
  
  elements.push(
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 50 },
      children: [
        new TextRun({
          text: caption,
          font: 'Calibri',
          size: 18,
          italics: true,
          color: COLORS.secondary
        })
      ]
    })
  );
  
  if (source) {
    elements.push(
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 200 },
        children: [
          new TextRun({
            text: `SOURCE: ${source}`,
            font: 'Calibri',
            size: 16,
            color: COLORS.secondary
          })
        ]
      })
    );
  }
  
  return elements;
};

const tableBorder = { style: BorderStyle.SINGLE, size: 1, color: 'CCCCCC' };
const cellBorders = { top: tableBorder, bottom: tableBorder, left: tableBorder, right: tableBorder };

const createTableCell = (text, isHeader = false) => {
  return new TableCell({
    borders: cellBorders,
    shading: { fill: isHeader ? COLORS.lightGray : COLORS.tableBg, type: ShadingType.CLEAR },
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 100, bottom: 100, left: 150, right: 150 },
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({
            text: text,
            font: 'Calibri',
            size: 18,
            bold: isHeader,
            color: isHeader ? COLORS.primary : COLORS.body
          })
        ]
      })
    ]
  });
};

// Main document generation
async function generateDocument() {
  console.log('Starting document generation...');
  
  // Read logo
  let logoBuffer;
  try {
    logoBuffer = fs.readFileSync(LOGO_PATH);
    console.log('Logo loaded successfully');
  } catch (e) {
    console.log('Logo not found, continuing without it');
  }

  const doc = new Document({
    styles: {
      default: {
        document: {
          run: { font: 'Times New Roman', size: 22 }
        }
      },
      paragraphStyles: [
        {
          id: 'Heading1',
          name: 'Heading 1',
          basedOn: 'Normal',
          next: 'Normal',
          quickFormat: true,
          run: { size: 32, bold: true, font: 'Times New Roman', color: COLORS.primary },
          paragraph: { spacing: { before: 400, after: 200 } }
        },
        {
          id: 'Heading2',
          name: 'Heading 2',
          basedOn: 'Normal',
          next: 'Normal',
          quickFormat: true,
          run: { size: 28, bold: true, font: 'Times New Roman', color: COLORS.primary },
          paragraph: { spacing: { before: 300, after: 150 } }
        },
        {
          id: 'Heading3',
          name: 'Heading 3',
          basedOn: 'Normal',
          next: 'Normal',
          quickFormat: true,
          run: { size: 24, bold: true, font: 'Times New Roman', color: COLORS.secondary },
          paragraph: { spacing: { before: 200, after: 100 } }
        }
      ]
    },
    sections: [
      // Cover Page Section
      {
        properties: {
          page: {
            margin: { top: 0, right: 0, bottom: 0, left: 0 }
          }
        },
        children: [
          new Paragraph({ spacing: { after: 1000 } }),
          ...(logoBuffer ? [
            new Paragraph({
              alignment: AlignmentType.CENTER,
              children: [
                new ImageRun({
                  type: 'png',
                  data: logoBuffer,
                  transformation: { width: 200, height: 80 },
                  altText: { title: 'CEDX Logo', description: 'CEDX Logo', name: 'logo' }
                })
              ]
            })
          ] : []),
          new Paragraph({ spacing: { after: 1500 } }),
          new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [
              new TextRun({
                text: 'CEDX RESEARCH REPORT',
                font: 'Times New Roman',
                size: 24,
                bold: true,
                color: COLORS.secondary
              })
            ]
          }),
          new Paragraph({ spacing: { after: 400 } }),
          new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [
              new TextRun({
                text: 'The 2026 Refinancing Wall',
                font: 'Times New Roman',
                size: 48,
                bold: true,
                color: COLORS.primary
              })
            ]
          }),
          new Paragraph({ spacing: { after: 200 } }),
          new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [
              new TextRun({
                text: 'Sovereign Debt Rollover Risks and Crisis Prevention in Emerging Markets',
                font: 'Times New Roman',
                size: 28,
                italics: true,
                color: COLORS.secondary
              })
            ]
          }),
          new Paragraph({ spacing: { after: 2000 } }),
          new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [
              new TextRun({
                text: 'Prepared by:',
                font: 'Times New Roman',
                size: 22,
                color: COLORS.body
              })
            ]
          }),
          new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [
              new TextRun({
                text: 'CEDX Research & Analysis Wing',
                font: 'Times New Roman',
                size: 24,
                bold: true,
                color: COLORS.primary
              })
            ]
          }),
          new Paragraph({ spacing: { after: 400 } }),
          new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [
              new TextRun({
                text: 'Date: January 2026 | Report No.: RR-CEDX-2026-013',
                font: 'Times New Roman',
                size: 20,
                color: COLORS.secondary
              })
            ]
          }),
          new Paragraph({ spacing: { after: 1000 } }),
          new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [
              new TextRun({
                text: 'Centre for Economic Development and Execution',
                font: 'Times New Roman',
                size: 20,
                bold: true,
                color: COLORS.accent
              })
            ]
          }),
          new Paragraph({ children: [new PageBreak()] })
        ]
      },
      // Main Content Section
      {
        properties: {
          page: {
            margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
          }
        },
        headers: {
          default: new Header({
            children: [
              new Paragraph({
                alignment: AlignmentType.RIGHT,
                children: [
                  new TextRun({
                    text: 'The 2026 Refinancing Wall | CEDX Research Report',
                    font: 'Calibri',
                    size: 18,
                    color: COLORS.secondary
                  })
                ]
              })
            ]
          })
        },
        footers: {
          default: new Footer({
            children: [
              new Paragraph({
                alignment: AlignmentType.CENTER,
                children: [
                  new TextRun({ text: 'Page ', font: 'Calibri', size: 18, color: COLORS.secondary }),
                  new TextRun({ children: [PageNumber.CURRENT], font: 'Calibri', size: 18, color: COLORS.secondary }),
                  new TextRun({ text: ' of ', font: 'Calibri', size: 18, color: COLORS.secondary }),
                  new TextRun({ children: [PageNumber.TOTAL_PAGES], font: 'Calibri', size: 18, color: COLORS.secondary })
                ]
              })
            ]
          })
        },
        children: [
          // Publication Information
          createHeading1('Publication Information'),
          createParagraph('For more information on this publication, visit: www.cedx.org/reports/RR-CEDX-2026-013'),
          createParagraph('Contact: info@cedx.org'),
          createHeading2('About CEDX'),
          createParagraph('The Centre for Economic Development and Execution (CEDX) is a nonprofit, nonpartisan research organization committed to advancing evidence-based policy solutions for sustainable economic development. Established in 2010, CEDX bridges the gap between rigorous academic research and practical policy implementation, serving governments, development finance institutions, and multilateral organizations across six continents. Our work spans macroeconomic policy, resource governance, institutional development, and climate economics, with a particular focus on emerging and frontier markets where strategic resource management determines development trajectories.'),
          createHeading2('Research Integrity'),
          createParagraph('CEDX maintains the highest standards of research integrity and methodological transparency. This report underwent a three-stage quality assurance process: (1) internal technical review by senior economists and governance specialists; (2) external peer review by three independent experts in resource economics and macroeconomic policy; (3) editorial review for accuracy and accessibility. All authors completed conflict-of-interest screenings, declaring no financial interests or advisory relationships that could influence findings. Independence safeguards include firewall protocols between research and funding units, and all quantitative analyses are reproducible with data and code available upon request.'),
          createHeading2('Disclaimer'),
          createParagraph('CEDX publications do not necessarily reflect the opinions of funders, sponsors, partners, or interview participants. Any errors are the responsibility of the authors alone. The analysis, findings, and recommendations contained herein represent the independent judgment of the research team based on available evidence as of December 2024.'),
          createHeading2('Copyright and Reuse'),
          createParagraph('© 2026 Centre for Economic Development and Execution (CEDX). The CEDX logo is a registered trademark. This report is provided for noncommercial use under Creative Commons Attribution-NonCommercial 4.0 International License.'),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // About This Report
          createHeading1('About This Report'),
          createHeading2('What Problem Does This Report Address?'),
          createParagraph('The refinancing wall confronting emerging markets in 2025-2028 represents a fundamental challenge to global financial stability. As the aggressive monetary tightening cycle of 2022-2024 pushed global interest rates to multi-decade highs, sovereigns across the developing world face a perfect storm: massive debt maturities coinciding with elevated borrowing costs, diminished risk appetite among international investors, and depleted foreign exchange reserves. This report addresses the critical question of which countries face rollover impossibility, when these pressures will peak, and what policy responses can prevent cascading defaults that would destabilize the global financial system and undermine development progress for billions of people.'),
          createParagraph('The stakes extend far beyond individual sovereign balance sheets. When countries lose market access and burn through reserves attempting to service unsustainable debt, the consequences cascade through banking systems, trade relationships, and political stability. The sovereign-corporate feedback loop amplifies initial shocks, as state-owned enterprise distress, banking sector deterioration, and contingent liability realization compound fiscal pressures. Understanding these dynamics and identifying intervention points before crisis becomes inevitable is essential for policymakers in both debtor and creditor nations.'),
          
          createHeading2('What Does This Report Do?'),
          createParagraph('This report provides a comprehensive analytical framework for assessing refinancing risks across emerging markets, with particular focus on the 2026 maturity wall. We reconstruct maturity profiles for the most vulnerable sovereigns, disaggregating obligations by instrument type (Eurobonds, external FX debt, local currency debt, SOE obligations) and time horizon. Our refinancing gap model quantifies the mismatch between financing needs and available resources under baseline and stress scenarios, identifying countries where intervention must precede market closure.'),
          createParagraph('Beyond quantitative analysis, we examine the rollover mechanics that transform financing challenges into systemic crises. Drawing on the sudden stop literature and risk premium dynamics, we model the transmission channels through which spread widening, auction failure, and reserve depletion interact to create self-reinforcing crisis dynamics. Four detailed case studies—Ghana, Sri Lanka, Zambia, and Pakistan—illustrate how these dynamics have unfolded in practice and what lessons they offer for crisis prevention.'),
          
          createHeading2('How Was This Research Conducted?'),
          createParagraph('Our methodology combines quantitative debt sustainability analysis with qualitative political economy assessment. We draw on primary data from sovereign debt offices, central banks, and multilateral institutions, supplemented by market data from Bloomberg and other financial information providers. The analysis covers the period 2019-2030, with particular emphasis on the 2025-2028 maturity window. Key analytical frameworks include the IMF Debt Sustainability Architecture, Assessing Reserve Adequacy metrics, and the Common Framework for debt treatment.'),
          createParagraph('Quantitative modules include Gross Financing Need calculations as a percentage of GDP, debt service to revenue ratios with explicit threshold analysis, and a refinancing gap model that stress-tests baseline assumptions against adverse scenarios (+300 basis points spread widening, 15 percent currency depreciation, 1.5 percentage point growth shortfall). We validate our findings against IMF program documents, market pricing, and the emerging empirical literature on recent sovereign restructurings.'),
          
          createHeading2('Who Is the Intended Audience?'),
          createParagraph('This report is designed for senior decision-makers in finance and foreign ministries, central banks, development finance institutions, and geopolitical strategy teams. The analysis assumes familiarity with sovereign debt concepts but provides sufficient background for cross-functional engagement. Technical appendices and supplementary data tables enable deeper dives for specialists while the executive summary and policy recommendations serve time-constrained readers.'),
          
          createHeading2('How to Navigate This Report'),
          createParagraph('Chapter 1 introduces the research context, objectives, and methodology. Chapter 2 establishes the economic and institutional baseline against which refinancing risks are assessed. Chapter 3 details our data sources and analytical methods. Chapter 4 presents core findings on maturity profiles and rollover analysis. Chapter 5 provides in-depth case studies of four vulnerable sovereigns. Chapter 6 addresses counterarguments and threshold analysis. Chapter 7 delivers policy recommendations and implementation guidance. Chapter 8 outlines execution and monitoring frameworks.'),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // Executive Summary
          createHeading1('Executive Summary'),
          createHeading2('Purpose and Scope'),
          createParagraph('This report provides a comprehensive assessment of sovereign refinancing risks in emerging markets, with particular focus on the 2026 maturity wall. We identify countries facing rollover impossibility, quantify financing gaps under baseline and stress scenarios, and deliver actionable policy recommendations for crisis prevention. The analysis covers seven primary case study countries (Ghana, Sri Lanka, Zambia, Pakistan, Kenya, Egypt, Nigeria) plus frontier Eurobond issuers with significant 2025-2027 maturities.'),
          
          createHeading2('Context'),
          createParagraph('The global monetary tightening cycle of 2022-2024 created unprecedented refinancing pressures for emerging market sovereigns. Federal Reserve policy rates rose from near-zero to over 5 percent, European Central Bank rates turned positive for the first time in a decade, and emerging market central banks followed suit to defend currencies and combat inflation. These higher rates coincided with massive debt maturities accumulated during the low-rate environment of the 2010s and the pandemic borrowing surge of 2020-2021. The result: a refinancing wall that threatens sovereign solvency across the developing world.'),
          createParagraph('Current approaches to sovereign debt sustainability focus on aggregate ratios (debt to GDP, external debt to exports) that mask timing vulnerabilities. Countries with seemingly sustainable aggregate positions may face acute rollover crises when maturities bunch, markets close, and reserves prove inadequate. The refinancing wall is fundamentally a timing problem—not merely "high debt" but debt maturing when refinancing conditions are unfavorable and alternatives are limited.'),
          
          createHeading2('Approach'),
          createParagraph('Our analytical framework proceeds through four stages: (1) maturity profile reconstruction, disaggregating obligations by instrument, currency, and time horizon; (2) rollover mechanics analysis, examining the channels through which financing pressures become crises; (3) quantitative stress testing, comparing baseline financing needs against adverse scenarios; and (4) policy option evaluation, assessing the effectiveness of preventive interventions.'),
          
          createHeading2('Key Findings'),
          createParagraph('Finding 1: The 2026 refinancing wall represents a systemic risk, with aggregate maturities across our sample exceeding $70 billion in that year alone—more than double the annual average from 2019-2023. Ghana, Pakistan, and Egypt face the largest absolute maturities, while Sri Lanka and Zambia confront the most constrained capacity to meet obligations.'),
          createParagraph('Finding 2: Gross Financing Needs exceed the 20 percent of GDP crisis threshold in four of seven countries in our sample for 2026, with Pakistan reaching 28.2 percent. These levels crowd out essential public investment and social spending, creating politically explosive tradeoffs.'),
          createParagraph('Finding 3: Debt service to revenue ratios exceed the 30 percent "politically explosive" threshold in Ghana, Sri Lanka, Pakistan, and Egypt throughout our projection period. Pakistan reaches 58.4 percent in 2026, meaning over half of government revenue services debt before any current spending occurs.'),
          createParagraph('Finding 4: FX reserve adequacy has deteriorated significantly, with three countries (Sri Lanka, Pakistan, Ghana) holding reserves below three months of imports—the conventional minimum threshold. Sri Lanka and Pakistan fail to cover even 30 percent of short-term external debt with reserves.'),
          createParagraph('Finding 5: The refinancing gap model reveals significant shortfalls under stress scenarios. Pakistan faces a $15.2 billion gap under stress conditions, while Ghana and Egypt confront gaps exceeding $8 billion. These gaps represent the resources that must be mobilized through IFI support, market access, or debt treatment to avoid default.'),
          createParagraph('Finding 6: The sovereign-corporate feedback loop amplifies refinancing risks through banking sector contagion, SOE distress, and contingent liability realization. Ghana\'s energy sector arrears and Pakistan\'s power sector circular debt exemplify how sovereign debt distress translates into broader economic dysfunction.'),
          createParagraph('Finding 7: Case studies reveal that early engagement with creditors and IFIs produces better outcomes than crisis-driven negotiations. Zambia\'s Common Framework process, while protracted, achieved deeper debt relief than would have been possible through bilateral negotiations alone.'),
          createParagraph('Finding 8: Preventive liability management—buybacks, exchanges, and maturity extensions before market closure—offers significant advantages over post-crisis restructuring. The key is identifying intervention triggers before reserves collapse and spreads reach distressed levels.'),
          
          createHeading2('Recommendations'),
          createParagraph('Recommendation 1: Establish pre-funding facilities before reserves drop below three months of imports. This threshold should trigger automatic engagement with IFIs and precautionary credit line negotiations.'),
          createParagraph('Recommendation 2: Implement liability management operations for 2026 maturities in the next 6-18 months, targeting maturity extension and spread reduction through voluntary exchanges.'),
          createParagraph('Recommendation 3: Deepen domestic debt markets through benchmark yield curve development, expanded investor base, and market-making infrastructure to enhance local currency financing capacity.'),
          createParagraph('Recommendation 4: Secure IMF/IFI contingent credit lines as credibility buffers, engaging before reserves collapse to preserve negotiating leverage.'),
          createParagraph('Recommendation 5: Develop FX hedging instruments for investors to reduce currency risk premium embedded in sovereign borrowing costs.'),
          createParagraph('Recommendation 6: Enhance debt transparency and reporting through public debt registries, timely disclosure, and independent debt management office capacity.'),
          createParagraph('Recommendation 7: Strengthen SOE governance and contingent liability management to prevent sovereign balance sheet contamination from parastatal distress.'),
          createParagraph('Recommendation 8: Establish sovereign contingency funds during favorable market conditions to build buffers for future shocks.'),
          
          createHeading2('Implementation at a Glance'),
          new Paragraph({ spacing: { after: 200 } }),
          new Table({
            columnWidths: [2000, 2000, 1500, 1500, 2000],
            rows: [
              new TableRow({
                tableHeader: true,
                children: [
                  createTableCell('Action', true),
                  createTableCell('Lead', true),
                  createTableCell('Timeframe', true),
                  createTableCell('Cost', true),
                  createTableCell('Outcome', true)
                ]
              }),
              new TableRow({
                children: [
                  createTableCell('Pre-funding facility'),
                  createTableCell('Ministry of Finance'),
                  createTableCell('0-6 months'),
                  createTableCell('$2-5bn'),
                  createTableCell('Avoid auction failure')
                ]
              }),
              new TableRow({
                children: [
                  createTableCell('Liability management'),
                  createTableCell('Debt Management Office'),
                  createTableCell('6-18 months'),
                  createTableCell('$50-100mn'),
                  createTableCell('Reduce rollover risk')
                ]
              }),
              new TableRow({
                children: [
                  createTableCell('Market deepening'),
                  createTableCell('Central Bank'),
                  createTableCell('12-36 months'),
                  createTableCell('$10-20mn'),
                  createTableCell('Expand local capacity')
                ]
              }),
              new TableRow({
                children: [
                  createTableCell('IMF/IFI engagement'),
                  createTableCell('Ministry of Finance'),
                  createTableCell('0-12 months'),
                  createTableCell('N/A'),
                  createTableCell('Credibility buffer')
                ]
              })
            ]
          }),
          createParagraph('SOURCE: CEDX Implementation Framework', { size: 18, color: COLORS.secondary }),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // Table of Contents
          createHeading1('Contents'),
          new TableOfContents('Table of Contents', {
            hyperlink: true,
            headingStyleRange: '1-3'
          }),
          new Paragraph({
            alignment: AlignmentType.CENTER,
            spacing: { before: 200 },
            children: [
              new TextRun({
                text: 'Note: Right-click and select "Update Field" to refresh page numbers.',
                font: 'Calibri',
                size: 18,
                italics: true,
                color: '999999'
              })
            ]
          }),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // Abbreviations
          createHeading1('Abbreviations'),
          new Table({
            columnWidths: [2000, 7000],
            rows: [
              new TableRow({ children: [createTableCell('Abbreviation', true), createTableCell('Full Term', true)] }),
              new TableRow({ children: [createTableCell('ARA'), createTableCell('Assessing Reserve Adequacy')] }),
              new TableRow({ children: [createTableCell('CAC'), createTableCell('Collective Action Clause')] }),
              new TableRow({ children: [createTableCell('DSA'), createTableCell('Debt Sustainability Analysis')] }),
              new TableRow({ children: [createTableCell('ECB'), createTableCell('European Central Bank')] }),
              new TableRow({ children: [createTableCell('EMBI'), createTableCell('Emerging Market Bond Index')] }),
              new TableRow({ children: [createTableCell('Fed'), createTableCell('Federal Reserve')] }),
              new TableRow({ children: [createTableCell('FX'), createTableCell('Foreign Exchange')] }),
              new TableRow({ children: [createTableCell('GFN'), createTableCell('Gross Financing Need')] }),
              new TableRow({ children: [createTableCell('GDP'), createTableCell('Gross Domestic Product')] }),
              new TableRow({ children: [createTableCell('IFI'), createTableCell('International Financial Institution')] }),
              new TableRow({ children: [createTableCell('IMF'), createTableCell('International Monetary Fund')] }),
              new TableRow({ children: [createTableCell('NPV'), createTableCell('Net Present Value')] }),
              new TableRow({ children: [createTableCell('SOE'), createTableCell('State-Owned Enterprise')] }),
              new TableRow({ children: [createTableCell('ST'), createTableCell('Short-Term')] })
            ]
          }),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // Chapter 1: Introduction
          createHeading1('Chapter 1. Introduction'),
          createParagraph('This chapter introduces the research context, objectives, and methodology for assessing the 2026 refinancing wall facing emerging market sovereigns. We establish the analytical framework and scope boundaries that guide subsequent analysis.'),
          
          createHeading2('1.1 Research Context and Motivation'),
          createParagraph('The global financial landscape has undergone a fundamental transformation since 2020. The COVID-19 pandemic triggered an unprecedented fiscal and monetary response, with governments worldwide expanding balance sheets to support households and businesses through lockdowns and supply disruptions. Emerging market sovereigns borrowed heavily in international markets, taking advantage of suppressed global interest rates and abundant liquidity. Total external debt stock in low- and middle-income countries reached $9.3 trillion by end-2023, with sovereign and sovereign-guaranteed obligations comprising the largest share.'),
          createParagraph('This borrowing surge, while necessary to address immediate crisis needs, has created a structural refinancing challenge that will define sovereign debt dynamics through the remainder of this decade. The maturities issued during 2020-2022 are now coming due, but the environment in which they must be rolled over has fundamentally changed. Central banks in advanced economies have executed the most aggressive tightening cycle in four decades, with the Federal Reserve raising policy rates from 0-0.25 percent in early 2022 to 5.25-5.50 percent by mid-2023. The European Central Bank, Bank of England, and other major central banks followed similar paths.'),
          createParagraph('The consequences for emerging markets have been severe. Higher global rates have increased borrowing costs across the yield curve, with sovereign spreads widening dramatically for vulnerable issuers. Currency depreciation has inflated the local currency cost of servicing external debt. Investor risk appetite has contracted, with capital flowing out of emerging market debt funds and into the attractive yields available on developed market sovereigns. Countries that borrowed at 5-6 percent during the low-rate environment now face refinancing at 10-15 percent—if they can access markets at all.'),
          createParagraph('This report addresses the fundamental question: which countries face rollover impossibility, and when? The answer matters enormously. Sovereign debt crises impose enormous costs on populations through austerity, inflation, and reduced public services. They spill over to banking systems, trade relationships, and regional stability. Early identification of vulnerabilities enables preventive action that can avoid the worst outcomes. Delayed response limits options and increases the probability of disorderly default.'),
          createParagraph('The refinancing wall is not simply a function of high debt ratios. Countries with seemingly sustainable debt-to-GDP levels may face acute rollover crises when maturities bunch and markets close. Conversely, countries with higher debt levels may successfully navigate refinancing if they maintain market access, reserve buffers, and credible policy frameworks. Understanding these dynamics requires moving beyond aggregate ratios to examine the timing, composition, and market context of sovereign obligations.'),
          
          createHeading2('1.2 Objectives and Research Questions'),
          createParagraph('The primary objective of this report is to provide decision-makers with a comprehensive analytical framework for assessing refinancing risks and identifying intervention opportunities. We seek to answer the following research questions:'),
          createParagraph('1. What is the magnitude and timing of the refinancing wall facing emerging market sovereigns in 2025-2028?'),
          createParagraph('2. Which countries face the greatest rollover impossibility risk, and what factors determine their vulnerability?'),
          createParagraph('3. How do the rollover mechanics transform financing pressures into systemic crises?'),
          createParagraph('4. What quantitative thresholds distinguish sustainable from unsustainable refinancing dynamics?'),
          createParagraph('5. What policy interventions can prevent refinancing crises, and when must they be implemented?'),
          createParagraph('6. What lessons do recent case studies offer for crisis prevention and resolution?'),
          createParagraph('This report makes several contributions to the literature and policy practice. First, we provide a granular maturity profile reconstruction that disaggregates sovereign obligations by instrument, currency, and time horizon—going beyond the aggregate ratios that dominate standard debt sustainability analysis. Second, we develop a refinancing gap model that explicitly compares financing needs against available resources under stress scenarios. Third, we identify explicit threshold values for early warning indicators that can trigger preventive action. Fourth, we translate analytical findings into actionable policy recommendations with specified implementation timelines and responsible parties.'),
          
          createHeading2('1.3 Scope, Definitions, and Assumptions'),
          createParagraph('This analysis covers the period 2019-2030, with particular emphasis on the 2025-2028 maturity window. The geographic scope encompasses emerging and frontier market sovereigns with significant external debt obligations and potential refinancing vulnerabilities. Our primary case study countries are Ghana, Sri Lanka, Zambia, and Pakistan—selected based on their recent crisis experiences and relevance to the 2026 refinancing wall. Secondary analysis covers Kenya, Egypt, and Nigeria, plus frontier Eurobond issuers with 2025-2027 maturities.'),
          createParagraph('Key definitions employed throughout this report:'),
          createParagraph('Refinancing Wall: The convergence of maturing debt obligations with unfavorable refinancing conditions, creating rollover impossibility for vulnerable sovereigns.'),
          createParagraph('Gross Financing Need (GFN): The total financing requirement in a given year, comprising debt amortization, interest payments, and the primary deficit. Expressed as a percentage of GDP for cross-country comparison.'),
          createParagraph('Rollover Impossibility: A situation where financing needs exceed available resources (market access, reserves, IFI support) at acceptable cost, requiring either debt treatment or default.'),
          createParagraph('Politically Explosive Threshold: The debt service to revenue ratio beyond which fiscal tradeoffs become unsustainable—typically identified as 25-30 percent based on historical evidence and political economy analysis.'),
          createParagraph('Several key assumptions underpin our analysis. We assume that global interest rates will remain elevated relative to the 2010-2021 period, with the Federal Funds rate stabilizing in the 3.5-4.5 percent range through 2026. We assume continued investor differentiation among emerging market sovereigns, with higher-rated issuers retaining market access while lower-rated issuers face periodic closure. We assume that IFI support remains available for countries implementing credible reform programs, though at levels that may not fully bridge financing gaps.'),
          
          createHeading2('1.4 Methodology Overview'),
          createParagraph('Our analytical framework integrates quantitative debt sustainability analysis with qualitative political economy assessment. The methodology proceeds through four stages:'),
          createParagraph('Stage 1: Maturity Profile Reconstruction. We compile comprehensive maturity profiles for each country, disaggregating obligations by instrument type (Eurobonds, external FX debt, local currency debt, SOE obligations), currency composition, and time horizon. Data sources include sovereign debt offices, central banks, IMF Debt Sustainability Analyses, Bloomberg market data, and World Bank International Debt Statistics.'),
          createParagraph('Stage 2: Rollover Mechanics Analysis. We examine the channels through which financing pressures become crises, drawing on the sudden stop literature and risk premium dynamics. Key transmission channels include spread widening effects on borrowing costs, auction failure risk, reserve adequacy dynamics, and banking sector spillovers.'),
          createParagraph('Stage 3: Quantitative Stress Testing. We develop a refinancing gap model that compares baseline financing needs against stress scenarios. Stress assumptions include: +300 basis points spread widening, 15 percent currency depreciation, and 1.5 percentage point growth shortfall. Results identify countries where intervention must precede market closure.'),
          createParagraph('Stage 4: Policy Option Evaluation. We assess the effectiveness of preventive interventions including liability management operations, IMF/IFI engagement, domestic market development, and creditor coordination mechanisms. Recommendations are prioritized based on impact, feasibility, cost, and timing constraints.'),
          
          // Add Figure 1.1
          ...createFigure(
            path.join(FIGURES_DIR, 'figure_1_1_conceptual_framework.png'),
            'Figure 1.1: The Refinancing Wall - Conceptual Framework',
            'CEDX Framework Analysis'
          ),
          
          createHeading2('1.5 How This Report Is Organized'),
          createParagraph('Chapter 2 establishes the economic and institutional context, presenting baseline indicators and trends across our sample countries. Chapter 3 details our data sources and analytical methods. Chapter 4 presents core findings on maturity profiles and rollover analysis. Chapter 5 provides in-depth case studies of four vulnerable sovereigns. Chapter 6 addresses counterarguments and threshold analysis. Chapter 7 delivers policy recommendations. Chapter 8 outlines execution and monitoring frameworks. Technical appendices provide supplementary data and methodological details.'),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // Chapter 2: Economic and Institutional Context
          createHeading1('Chapter 2. Economic and Institutional Context'),
          createParagraph('This chapter establishes the baseline economic conditions and institutional frameworks against which refinancing risks are assessed. Understanding the starting point is essential for evaluating financing needs and identifying intervention opportunities.'),
          
          createHeading2('2.1 Baseline Indicators and Trends'),
          createParagraph('The countries in our sample exhibit significant heterogeneity in economic structure, debt composition, and institutional capacity. Table 2.1 presents key baseline indicators as of end-2024, highlighting the diverse challenges facing each sovereign. Ghana entered 2025 with public debt at 84.9 percent of GDP following its 2022 default and ongoing restructuring process. The country\'s Eurobond spreads remain elevated at approximately 1,800 basis points, reflecting market concerns about implementation risks and the path back to market access. Foreign exchange reserves of $5.8 billion cover just 2.8 months of imports—well below the conventional three-month minimum threshold.'),
          createParagraph('Sri Lanka remains in default on its external commercial debt, with restructuring negotiations ongoing following the comprehensive economic crisis of 2022. Public debt exceeds 100 percent of GDP, though the restructuring is expected to provide significant NPV relief. Foreign exchange reserves have partially recovered from crisis lows but remain inadequate at $2.5 billion (1.9 months of imports). The country\'s return to capital markets depends critically on successful restructuring completion and IMF program performance.'),
          createParagraph('Zambia completed its Common Framework restructuring in 2024, achieving meaningful relief on bilateral debt and setting the template for Eurobond treatment. Public debt remains elevated at 98.7 percent of GDP, but the debt service trajectory has improved substantially. Copper sector performance and global commodity prices will be critical determinants of the country\'s refinancing capacity.'),
          createParagraph('Pakistan faces chronic external imbalances that have required continuous IMF engagement. Public debt at 77.6 percent of GDP is moderate by regional standards, but the debt service burden is crushing—over 50 percent of government revenue services debt before any current spending occurs. Foreign exchange reserves of $7.5 billion cover just 1.3 months of imports, leaving the country vulnerable to any deterioration in external conditions.'),
          createParagraph('Kenya successfully navigated its June 2024 Eurobond maturity through a combination of buyback and new issuance, demonstrating that proactive liability management can avoid crisis. However, the country faces additional maturities in coming years and maintains elevated debt service ratios. Egypt has received substantial Gulf investment and IMF support, but external vulnerability persists with external debt at 42.3 percent of GDP and reserves covering 3.2 months of imports. Nigeria benefits from oil export revenues that support larger reserve buffers, but the country faces domestic debt sustainability challenges and currency pressures.'),
          
          // Add Figure 2.1
          ...createFigure(
            path.join(FIGURES_DIR, 'figure_2_1_global_interest_rates.png'),
            'Figure 2.1: Global Interest Rate Trends (2019-2026)',
            'Federal Reserve, ECB, Bank of England, IMF'
          ),
          
          createParagraph('Figure 2.1 illustrates the dramatic shift in global monetary conditions. The Federal Funds rate rose from near-zero in early 2022 to over 5 percent by mid-2023—the most aggressive tightening cycle in four decades. This rate environment fundamentally alters refinancing conditions for emerging market sovereigns. Bonds issued at 5-6 percent during the low-rate environment must now be refinanced at 10-15 percent if market access is available, dramatically increasing debt service costs and fiscal pressure.'),
          
          // Add Figure 2.2
          ...createFigure(
            path.join(FIGURES_DIR, 'figure_2_2_sovereign_spreads.png'),
            'Figure 2.2: Sovereign Spread Evolution (2020-2025)',
            'Bloomberg, JPMorgan EMBI'
          ),
          
          createParagraph('Sovereign spreads have reflected these changed conditions with significant differentiation among issuers. Figure 2.2 shows the spread trajectory for EMBI Global and selected vulnerable sovereigns. The 2022 crisis period saw spreads spike across the board, with Ghana, Sri Lanka, and Zambia reaching distressed levels above 2,500 basis points. While spreads have partially normalized, they remain well above pre-crisis levels for vulnerable issuers. This elevated spread environment directly translates into higher refinancing costs and constrained market access.'),
          
          createHeading2('2.2 Policy, Regulatory, and Institutional Landscape'),
          createParagraph('The institutional capacity to manage refinancing challenges varies significantly across our sample countries. Ghana\'s debt management office has benefited from technical assistance under the IMF program, but implementation capacity remains constrained by fiscal pressures. Sri Lanka is rebuilding institutional capacity following the crisis-induced collapse of state functions in 2022. Zambia\'s debt office gained experience through the protracted Common Framework process, though capacity gaps persist. Pakistan\'s institutional framework is relatively developed but hampered by political instability and fiscal constraints.'),
          createParagraph('Legal frameworks for debt management differ across jurisdictions. Some countries have enacted comprehensive public debt management laws that mandate transparency, set borrowing limits, and establish accountability mechanisms. Others operate under executive decrees or fragmented legislative frameworks that complicate debt governance. These institutional differences affect both the ability to implement preventive measures and the credibility of commitments to creditors.'),
          createParagraph('The regulatory environment for domestic debt markets presents both opportunities and constraints. Countries with developed local currency bond markets have more options for liability management and refinancing. Kenya\'s domestic market, for instance, has sufficient depth to absorb significant government issuance. Other countries face shallower markets with limited investor bases, constraining their ability to substitute local for external financing.'),
          
          createHeading2('2.3 Stakeholder and Political Economy Analysis'),
          createParagraph('Refinancing decisions are inherently political as well as economic. Debt service crowds out other spending priorities, forcing governments to make difficult tradeoffs between creditors and citizens. The political economy of these tradeoffs varies across countries depending on fiscal space, social contract expectations, and the composition of affected stakeholders.'),
          createParagraph('In countries where debt service exceeds 40 percent of revenue, the political sustainability of current arrangements becomes questionable. Essential public services, infrastructure investment, and social programs must compete for the remaining fiscal space. When this competition intensifies—often triggered by external shocks or domestic political events—the social contract comes under strain. Sri Lanka\'s 2022 crisis exemplified this dynamic, as debt service constraints combined with other economic pressures to trigger mass protests and political collapse.'),
          createParagraph('The creditor landscape also shapes refinancing dynamics. Traditional Paris Club bilateral creditors have been supplemented—indeed, in some cases supplanted—by non-Paris Club sovereign lenders (particularly China) and private creditors holding Eurobonds. This fragmentation complicates coordinated debt treatment, as different creditor classes have different interests, instruments, and institutional frameworks. The Common Framework represents an attempt to coordinate treatment across creditor classes, but implementation challenges persist.'),
          
          createHeading2('2.4 Key Constraints and Opportunity Areas'),
          createParagraph('Several cross-cutting constraints shape the refinancing landscape across our sample countries. Limited reserve buffers constrain the ability to bridge temporary market closures. Shallow domestic markets limit substitution toward local currency financing. Political economy pressures complicate the fiscal adjustment needed to restore sustainability. Fragmented creditor coordination increases the complexity of any debt treatment.'),
          createParagraph('Opportunity areas exist alongside these constraints. Technical assistance from IFIs has improved debt management capacity in several countries. Liability management tools—buybacks, exchanges, and maturity extensions—offer preventive options that can reduce rollover concentration. Domestic market development, while slow, can gradually expand local financing options. Regional financial integration may provide alternative funding sources. The key is identifying intervention points where action can prevent crisis rather than respond to it.'),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // Chapter 3: Methods and Data
          createHeading1('Chapter 3. Methods and Data'),
          createParagraph('This chapter details the research design, data sources, and analytical methods employed in this study. Transparency about methodology enables readers to assess the reliability of findings and the applicability of conclusions to specific contexts.'),
          
          createHeading2('3.1 Study Design'),
          createParagraph('This study employs a mixed-methods approach combining quantitative debt sustainability analysis with qualitative case study research. The quantitative component provides structured, comparable metrics across countries and time periods. The qualitative component adds depth and context, examining how refinancing dynamics have unfolded in specific cases and identifying factors that quantitative indicators may miss.'),
          createParagraph('The study design proceeds through four analytical stages: (1) descriptive analysis establishing baseline conditions and maturity profiles; (2) diagnostic analysis identifying vulnerability factors and their interactions; (3) predictive analysis projecting financing needs under baseline and stress scenarios; and (4) prescriptive analysis evaluating policy options and implementation requirements.'),
          
          createHeading2('3.2 Data Sources'),
          createParagraph('Primary data sources include: Sovereign debt offices and central banks for official debt statistics and maturity profiles; International Monetary Fund for Debt Sustainability Analyses, program documents, and Article IV consultations; World Bank for International Debt Statistics, Worldwide Governance Indicators, and macroeconomic data; Bloomberg for market data including bond prices, yields, and spreads.'),
          createParagraph('Secondary sources include: Academic literature on sovereign debt sustainability, sudden stops, and debt restructuring; Policy reports from IFIs, think tanks, and research institutions; Media coverage of sovereign debt developments; Expert interviews conducted with practitioners and analysts.'),
          createParagraph('Data quality and availability vary across countries. Countries with IMF programs typically have more comprehensive and timely data disclosure. Countries in default or distress may have data gaps reflecting administrative capacity constraints. Where data inconsistencies arise, we note them and apply conservative assumptions.'),
          
          createHeading2('3.3 Analytical Methods'),
          createParagraph('Gross Financing Need (GFN) calculations follow the standard IMF methodology: GFN = Amortization + Interest Payments + Primary Deficit. This measure captures the total financing requirement in a given year, enabling comparison of financing pressure across countries and time periods. We express GFN as a percentage of GDP to normalize for country size.'),
          createParagraph('Debt service to revenue ratios are calculated as: (Interest Payments + Amortization) / Government Revenue. This measure captures the fiscal burden of debt service, indicating the extent to which debt obligations crowd out other spending. We identify explicit thresholds (25 percent and 30 percent) based on political economy literature and historical evidence of fiscal stress.'),
          createParagraph('The refinancing gap model compares financing needs against available resources: Gap = GFN - (Market Access + Reserves + IFI Support + Other Sources). Under stress scenarios, we apply adjustments to each component: market access is reduced by 50 percent (reflecting potential market closure); reserves are drawn down by 30 percent (reflecting defense of currency); IFI support is maintained at baseline (reflecting program constraints).'),
          createParagraph('Stress scenario assumptions are calibrated to historical experience: +300 basis points spread widening reflects the average increase during risk-off episodes; 15 percent currency depreciation reflects typical emerging market FX stress; 1.5 percentage point growth shortfall reflects the output gap during debt distress episodes.'),
          
          createHeading2('3.4 Limitations'),
          createParagraph('Several limitations constrain the analysis. Data availability varies across countries, particularly for contingent liabilities and SOE obligations. Maturity profiles may be incomplete where debt offices lack comprehensive reporting systems. Market access is difficult to predict ex-ante, making scenario analysis inherently uncertain. Political economy factors are difficult to quantify, requiring qualitative judgment. The analysis cannot capture all relevant factors, and findings should be interpreted as indicative rather than definitive.'),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // Chapter 4: Findings
          createHeading1('Chapter 4. Findings: Maturity Profile and Rollover Analysis'),
          createParagraph('This chapter presents the core analytical findings on maturity profiles, refinancing needs, and rollover dynamics. We begin with aggregate patterns before examining country-specific results.'),
          
          createHeading2('4.1 Maturity Profile Reconstruction'),
          createParagraph('The aggregate maturity wall across our sample countries reveals significant concentration in the 2025-2028 period. Figure 4.1 presents the combined maturity profile by instrument type, showing total obligations exceeding $70 billion in 2026 alone—a dramatic increase from the $35-40 billion annual average during 2019-2023. This concentration reflects the pandemic-era borrowing surge now coming due in a fundamentally different rate environment.'),
          
          // Add Figure 4.1
          ...createFigure(
            path.join(FIGURES_DIR, 'figure_4_1_aggregate_maturity_wall.png'),
            'Figure 4.1: Aggregate Debt Maturity Wall (All Countries)',
            'Country debt offices, IMF DSA, Bloomberg'
          ),
          
          createParagraph('The composition of maturities matters as much as the aggregate amount. Eurobonds, representing the most market-sensitive obligations, show particular concentration in 2026-2027. Countries that issued five-year paper during the pandemic boom of 2020-2021 now face refinancing in a far less favorable environment. External FX debt from bilateral and commercial creditors adds to the refinancing challenge, though some bilateral obligations may be restructured through official channels. Local currency debt can theoretically be refinanced through domestic markets, but capacity varies significantly across countries. SOE obligations represent contingent liabilities that may crystallize on sovereign balance sheets during stress periods.'),
          
          createParagraph('Figure 4.2 disaggregates the maturity wall by country, revealing heterogeneous patterns. Pakistan faces the largest absolute maturities, driven by substantial local currency debt and a significant external FX burden. Ghana\'s Eurobond maturities concentrate in 2026 and 2028, creating rollover spikes. Sri Lanka\'s Eurobond obligations are currently in default with treatment pending, but external FX and local currency maturities persist. Zambia\'s Common Framework restructuring has modified its maturity profile, but obligations remain substantial.'),
          
          // Add Figure 4.2
          ...createFigure(
            path.join(FIGURES_DIR, 'figure_4_2_country_maturity_walls.png'),
            'Figure 4.2: Country-Level Debt Maturity Walls',
            'Country debt offices, IMF DSA'
          ),
          
          createHeading2('4.2 Gross Financing Needs Analysis'),
          createParagraph('Gross Financing Need provides a comprehensive measure of annual financing pressure. Figure 4.3 presents GFN as a percentage of GDP for each country across the projection period. Four countries—Ghana, Pakistan, Kenya, and Egypt—exceed the 20 percent crisis threshold in 2026, indicating acute refinancing pressure that cannot be met through routine operations.'),
          
          // Add Figure 4.3
          ...createFigure(
            path.join(FIGURES_DIR, 'figure_4_3_gross_financing_needs.png'),
            'Figure 4.3: Gross Financing Needs (% GDP) by Country',
            'IMF DSA, World Bank, CEDX Calculations'
          ),
          
          createParagraph('Pakistan\'s GFN reaches 28.2 percent of GDP in 2026—the highest in our sample. This extraordinary figure reflects the combination of large maturities, elevated interest costs, and persistent primary deficits. At this level, over a quarter of national output must be mobilized through borrowing or other financing sources, an obviously unsustainable dynamic. Ghana\'s GFN peaks at 22.4 percent in 2026, driven by Eurobond maturities that must be addressed through restructuring or refinancing.'),
          createParagraph('The GFN trajectory matters as much as the level. Countries with declining GFN can reasonably expect improved financing conditions over time. Countries with stable or rising GFN face persistent pressure that may eventually exhaust buffers and creditor patience. Kenya\'s GFN declines from 16.8 percent in 2025 to 13.5 percent in 2027, reflecting successful navigation of the 2024 Eurobond maturity. Egypt\'s GFN remains persistently elevated above 22 percent, indicating structural financing challenges.'),
          
          createHeading2('4.3 Debt Service Sustainability'),
          createParagraph('Debt service to revenue ratios reveal the fiscal burden of sovereign obligations. Figure 4.4 presents these ratios with explicit threshold analysis. The 25 percent threshold marks the level beyond which debt service crowds out essential public services—police, healthcare, education, infrastructure maintenance. The 30 percent threshold marks "politically explosive" territory, where fiscal tradeoffs become unsustainable and social stability risks intensify.'),
          
          // Add Figure 4.4
          ...createFigure(
            path.join(FIGURES_DIR, 'figure_4_4_debt_service_revenue_ratio.png'),
            'Figure 4.4: Debt Service to Revenue Ratio',
            'IMF DSA, Ministry of Finance data'
          ),
          
          createParagraph('Pakistan\'s debt service burden is particularly striking at 58.4 percent of revenue in 2026. This means that nearly six out of every ten rupees collected by the government services debt before any current spending occurs. The remaining fiscal space must cover civil service salaries, defense, subsidies, development programs, and all other government functions. At these levels, fiscal policy becomes essentially about debt management rather than public service delivery.'),
          createParagraph('Ghana, Sri Lanka, and Egypt also breach the 30 percent threshold throughout the projection period. Sri Lanka\'s ratio declines from 52.4 percent in 2024 toward 38 percent by 2028, reflecting expected restructuring relief. Ghana\'s ratio peaks at 48.2 percent in 2026 before declining as Eurobond maturities are addressed. Kenya and Nigeria remain below but close to the 25 percent threshold, warranting careful monitoring.'),
          
          createHeading2('4.4 Stress Scenario Analysis'),
          createParagraph('The baseline scenario assumes continued market access at current spread levels, modest reserve utilization, and growth consistent with IMF projections. Stress scenarios test vulnerability to adverse developments. Figure 4.5 presents debt service trajectories for Ghana under baseline, moderate stress, and severe stress scenarios.'),
          
          // Add Figure 4.5
          ...createFigure(
            path.join(FIGURES_DIR, 'figure_4_5_stress_scenario_fan_chart.png'),
            'Figure 4.5: Ghana Debt Service Trajectories Under Stress Scenarios',
            'CEDX Stress Model'
          ),
          
          createParagraph('Under the severe stress scenario (+300bps spreads, -15% FX, -1.5pp growth), Ghana\'s debt service rises to $8.5 billion in 2026 compared to $5.5 billion under baseline. This $3 billion difference represents resources that must be mobilized through additional borrowing, reserve drawdown, or debt treatment. Similar dynamics apply across our sample, with stress scenarios generating significantly larger financing gaps.'),
          createParagraph('Figure 4.6 presents refinancing gap results across countries. The gap measures the difference between financing needs and available resources under each scenario. Pakistan faces the largest gap at $15.2 billion under stress conditions—a figure that exceeds total reserve holdings. Ghana and Egypt also show significant gaps exceeding $8 billion under stress.'),
          
          // Add Figure 4.6
          ...createFigure(
            path.join(FIGURES_DIR, 'figure_4_6_refinancing_gap_results.png'),
            'Figure 4.6: Refinancing Gap Model Results',
            'CEDX Refinancing Gap Model'
          ),
          
          createHeading2('4.5 Reserve Adequacy and Market Access'),
          createParagraph('Foreign exchange reserves provide the first line of defense against temporary market closures. Countries with adequate reserves can bridge financing gaps while awaiting improved market conditions or IFI support. Countries with depleted reserves have no buffer and must either secure immediate financing or default. Figure 4.7 compares external and local market rollover capacity against needs.'),
          
          // Add Figure 4.7
          ...createFigure(
            path.join(FIGURES_DIR, 'figure_4_7_rollover_capacity.png'),
            'Figure 4.7: External vs Local Market Rollover Capacity',
            'Central bank data, CEDX analysis'
          ),
          
          createParagraph('Reserve adequacy indicators reveal significant vulnerabilities. Figure 4.8 presents two standard metrics: months of import coverage and short-term debt coverage. Three countries—Sri Lanka, Pakistan, and Ghana—fall below the critical three-month import threshold. Pakistan and Sri Lanka fail to cover even 30 percent of short-term external debt with reserves, leaving them acutely vulnerable to any deterioration in market conditions.'),
          
          // Add Figure 4.8
          ...createFigure(
            path.join(FIGURES_DIR, 'figure_4_8_fx_reserve_adequacy.png'),
            'Figure 4.8: FX Reserve Adequacy Indicators',
            'IMF, Central Bank data'
          ),
          
          createHeading2('4.6 The Sovereign-Corporate Feedback Loop'),
          createParagraph('Refinancing risks do not remain confined to sovereign balance sheets. The sovereign-corporate feedback loop amplifies and transmits distress through multiple channels. When sovereign spreads widen, private sector borrowing costs rise in parallel—both because of implicit sovereign ceilings on credit ratings and because domestic banks, often major holders of government debt, see their balance sheets deteriorate.'),
          
          // Add Figure 5.2
          ...createFigure(
            path.join(FIGURES_DIR, 'figure_5_2_sovereign_corporate_loop.png'),
            'Figure 5.2: Sovereign-Corporate Feedback Loop',
            'CEDX Analysis'
          ),
          
          createParagraph('State-owned enterprises represent a particularly important transmission channel. SOE obligations often carry implicit sovereign guarantees that become explicit during stress periods. Ghana\'s energy sector arrears, estimated at over $2 billion, exemplify how SOE distress contaminates sovereign balance sheets. Pakistan\'s power sector circular debt presents a similar challenge, with accumulated arrears exceeding $10 billion.'),
          createParagraph('The banking sector creates another amplification channel. Banks in emerging markets typically hold significant government bond portfolios. When sovereign distress causes bond prices to fall, bank balance sheets deteriorate, potentially requiring sovereign support that further strains public finances. This circular dynamic can transform sovereign stress into systemic financial crisis.'),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // Chapter 5: Case Studies
          createHeading1('Chapter 5. Case Studies'),
          createParagraph('This chapter provides in-depth analysis of four sovereign debt cases that illuminate the dynamics of refinancing distress and crisis resolution. Each case demonstrates different aspects of the refinancing wall and offers lessons for prevention and response.'),
          
          createHeading2('5.1 Ghana: The Eurobond Maturity Challenge'),
          createParagraph('Ghana\'s debt trajectory exemplifies how the refinancing wall can emerge even in a country with strong growth potential and democratic institutions. Public debt rose from 62 percent of GDP in 2019 to over 100 percent by end-2022, driven by pandemic-related spending, energy sector arrears, and currency depreciation. The country lost market access in late 2022 as spreads exceeded 3,000 basis points, making Eurobond refinancing economically impossible.'),
          
          // Add Figure 6.1
          ...createFigure(
            path.join(FIGURES_DIR, 'figure_6_1_ghana_case_study.png'),
            'Figure 6.1: Ghana - Refinancing Wall Analysis',
            'IMF, Bank of Ghana, CEDX Analysis'
          ),
          
          createParagraph('Ghana\'s restructuring approach combined domestic debt exchange with external debt treatment under the Common Framework. The domestic exchange, completed in early 2023, achieved meaningful relief but at significant cost to the banking sector. External treatment negotiations are ongoing, with bilateral creditors agreeing to terms in 2024 and Eurobond treatment pending. The process illustrates both the challenges of coordinating across creditor classes and the potential for meaningful debt relief through structured frameworks.'),
          createParagraph('Key lessons from Ghana include: (1) Early engagement with IFIs and creditors produces better outcomes than delayed action; (2) Domestic debt exchanges have financial sector implications that must be managed; (3) Common Framework coordination is slow but can achieve deeper relief than bilateral approaches; (4) Return to market access requires demonstrated implementation capacity.'),
          
          createHeading2('5.2 Sri Lanka: Post-Default Restructuring'),
          createParagraph('Sri Lanka\'s 2022 crisis represents the most severe example of refinancing wall dynamics in our sample. The country faced a perfect storm of external shocks—tourism collapse, rising energy prices, and global monetary tightening—that exposed underlying structural vulnerabilities. Foreign exchange reserves fell to near-zero, forcing the country into a preemptive default on all external debt.'),
          
          // Add Figure 6.2
          ...createFigure(
            path.join(FIGURES_DIR, 'figure_6_2_sri_lanka_case_study.png'),
            'Figure 6.2: Sri Lanka - Refinancing Wall Analysis',
            'IMF, Central Bank of Sri Lanka'
          ),
          
          createParagraph('The restructuring process has been protracted, complicated by political instability, weak administrative capacity, and the need for comprehensive treatment across creditor classes. Bilateral creditors reached agreement in 2024, but Eurobond treatment remains pending. The country\'s experience illustrates how political factors interact with economic dynamics—the government that negotiated the IMF program was ousted by protests, creating uncertainty about implementation commitments.'),
          createParagraph('Key lessons from Sri Lanka include: (1) Political instability accelerates and deepens economic crisis; (2) Reserve depletion eliminates policy options; (3) Comprehensive debt treatment requires addressing both external and domestic obligations; (4) IMF program implementation provides credibility anchor during restructuring.'),
          
          createHeading2('5.3 Zambia: Common Framework Pioneer'),
          createParagraph('Zambia became the first African country to complete a Common Framework restructuring in 2024, setting an important precedent for coordinated treatment across creditor classes. The country defaulted on its Eurobonds in 2020 after years of deteriorating fiscal conditions and rising debt service burdens. The restructuring process took nearly four years, reflecting both the complexity of coordinating diverse creditors and Zambia\'s own capacity constraints.'),
          
          // Add Figure 6.3
          ...createFigure(
            path.join(FIGURES_DIR, 'figure_6_3_zambia_case_study.png'),
            'Figure 6.3: Zambia - Refinancing Wall Analysis',
            'IMF, Bank of Zambia'
          ),
          
          createParagraph('The Common Framework process achieved meaningful NPV relief through maturity extensions and coupon reductions. However, the protracted timeline imposed costs—uncertainty during negotiations discouraged investment, and the government operated under severe fiscal constraints. The process also highlighted coordination challenges with non-Paris Club bilateral creditors, particularly China, whose lending practices differ from traditional official creditors.'),
          createParagraph('Key lessons from Zambia include: (1) Common Framework can achieve meaningful relief but is slow; (2) Non-Paris Club creditor coordination remains challenging; (3) Commodity dependence creates additional volatility in debt sustainability; (4) Early engagement with all creditor classes accelerates resolution.'),
          
          createHeading2('5.4 Pakistan: Chronic External Imbalance'),
          createParagraph('Pakistan presents a different profile from the other case studies—not acute crisis but chronic vulnerability requiring continuous management. The country has operated under IMF programs for most of the past three decades, reflecting persistent external imbalances and fiscal deficits. Debt sustainability depends critically on maintaining program performance and securing periodic rollovers from bilateral partners, particularly China and Gulf states.'),
          
          // Add Figure 6.4
          ...createFigure(
            path.join(FIGURES_DIR, 'figure_6_4_pakistan_case_study.png'),
            'Figure 6.4: Pakistan - Refinancing Wall Analysis',
            'IMF, State Bank of Pakistan'
          ),
          
          createParagraph('Pakistan\'s 2026 Eurobond maturities ($2.8 billion) represent a significant refinancing challenge, but the larger burden comes from bilateral and commercial external debt plus persistent local currency refinancing needs. The country\'s debt service to revenue ratio exceeds 50 percent, indicating fiscal stress that cannot continue indefinitely. However, Pakistan\'s strategic importance provides access to financing that might not be available on purely economic criteria.'),
          createParagraph('Key lessons from Pakistan include: (1) Preventive action is superior to crisis response; (2) Political consensus enables sustained reform implementation; (3) Diversification of creditor base provides resilience; (4) Structural reforms are necessary to break cycle of chronic vulnerability.'),
          
          createHeading2('5.5 Frontier Eurobond Issuers Analysis'),
          createParagraph('Beyond our primary case studies, several frontier market Eurobond issuers face significant maturities in the 2025-2027 window. These include Ethiopia ($1 billion due 2024, now in default), Kenya (successfully refinanced 2024 maturity), Tunisia (ongoing restructuring), and various smaller issuers. The pattern across these cases reinforces our core findings: countries that engaged early with liability management and IFI support achieved better outcomes than those that delayed until market closure.'),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // Chapter 6: Counterarguments
          createHeading1('Chapter 6. Counterarguments and Risk Analysis'),
          createParagraph('This chapter addresses the primary counterargument to our thesis and examines the thresholds at which refinancing becomes impossible rather than merely expensive.'),
          
          createHeading2('6.1 "Markets Refinance at Some Price"'),
          createParagraph('The most common counterargument to refinancing wall concerns holds that markets will always provide financing at some price. This argument correctly notes that sovereigns rarely face absolute market closure—rather, they face closure at acceptable prices. A sovereign willing to pay 20 percent yields can likely find lenders, at least until the debt service burden from such rates becomes unsustainable.'),
          createParagraph('This argument has merit but ignores critical constraints. First, there is a threshold spread beyond which financing becomes economically impossible—where the cost of new borrowing exceeds the fiscal capacity to service it. Second, there is a threshold beyond which financing becomes politically impossible—where governments cannot credibly commit to the austerity required to service high-cost debt. Third, market access is not continuous but discontinuous: once spreads cross certain thresholds, the pool of willing lenders shrinks dramatically, and auction failure becomes a meaningful risk.'),
          createParagraph('Our analysis suggests that the "refinance at some price" argument fails when: (1) Debt service exceeds 40-50 percent of revenue, leaving insufficient fiscal space for essential functions; (2) Reserves fall below three months of imports, removing the buffer against temporary disruptions; (3) Spreads exceed 1,500-2,000 basis points, making new borrowing clearly unsustainable; (4) Political instability prevents credible commitment to reform programs. These thresholds are not hard rules but indicators that refinancing is transitioning from expensive to impossible.'),
          
          createHeading2('6.2 Threshold Analysis'),
          createParagraph('We identify explicit threshold values for early warning indicators that should trigger preventive action. These thresholds draw on historical experience, political economy analysis, and practical constraints identified in our case studies.'),
          createParagraph('Reserve adequacy thresholds: Three months of imports represents the conventional minimum, but countries with current account deficits and external debt service should hold more. The IMF\'s Assessing Reserve Adequacy metric provides a more comprehensive framework incorporating short-term debt, portfolio flows, and export volatility. Countries falling below these thresholds face elevated rollover risk.'),
          createParagraph('Debt service thresholds: The 25 percent of revenue threshold marks the point where debt service crowds out essential public services. The 30 percent threshold marks "politically explosive" territory where fiscal tradeoffs become unsustainable. Countries exceeding these thresholds require either debt relief or exceptional revenue mobilization.'),
          createParagraph('Spread thresholds: Spreads above 1,000 basis points indicate distressed territory where market access becomes limited. Spreads above 2,000 basis points indicate near-certain market closure for new issuance. Countries crossing these thresholds must secure alternative financing sources or restructure.'),
          
          createHeading2('6.3 Risk Premium Dynamics'),
          createParagraph('Sovereign risk premiums are not static but dynamic—affected by global risk appetite, domestic fundamentals, and self-fulfilling expectations. A country with marginally sustainable debt may see spreads widen dramatically if investors perceive elevated rollover risk, creating a self-reinforcing cycle where higher spreads increase financing costs, which increases debt service burdens, which justifies higher spreads.'),
          createParagraph('This dynamic explains why refinancing walls can materialize suddenly rather than gradually. A country that appears sustainable under current spreads may become unsustainable when spreads widen, but the spread widening itself is triggered by concerns about refinancing capacity. Breaking this cycle requires either external support that provides credible financing guarantees or preemptive debt treatment that reduces refinancing needs.'),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // Chapter 7: Recommendations
          createHeading1('Chapter 7. Recommendations and Policy Options'),
          createParagraph('This chapter translates analytical findings into actionable policy recommendations, organized by intervention type and implementation timeline.'),
          
          createHeading2('7.1 Liability Management Menu'),
          createParagraph('Preventive liability management offers significant advantages over post-crisis restructuring. Operations conducted while market access remains possible can achieve maturity extension, cost reduction, and risk mitigation at lower transaction costs and with less economic disruption. Figure 7.1 presents the menu of liability management options available to sovereigns.'),
          
          // Add Figure 7.1
          ...createFigure(
            path.join(FIGURES_DIR, 'figure_7_1_liability_menu.png'),
            'Figure 7.1: Liability Management Menu',
            'CEDX Liability Management Toolkit'
          ),
          
          createParagraph('Buybacks involve purchasing existing debt at market prices, typically when bonds trade below par. This reduces outstanding stock and can demonstrate confidence to markets. Ghana conducted selective buybacks of local currency debt before its 2023 restructuring. Cash buffers involve pre-funding future maturities through current borrowing, building reserves that can meet obligations even if markets temporarily close. Kenya\'s 2024 Eurobond refinancing exemplified this approach.'),
          createParagraph('Exchanges involve swapping existing bonds for new instruments with modified terms—extended maturities, adjusted coupons, or changed currency. Uruguay\'s 2003 exchange set the template for successful preventive operations. Extensions through consent solicitations can push back maturities without full exchange, useful when only timing is problematic rather than sustainability.'),
          
          createHeading2('7.2 IMF/IFI Engagement Sequencing'),
          createParagraph('International financial institutions provide essential support for countries facing refinancing pressures, but engagement must be properly timed. Figure 7.2 presents the recommended sequencing of IFI engagement relative to reserve and spread thresholds.'),
          
          // Add Figure 7.2
          ...createFigure(
            path.join(FIGURES_DIR, 'figure_7_2_imf_engagement.png'),
            'Figure 7.2: IMF/IFI Engagement Sequencing',
            'CEDX IFI Engagement Framework'
          ),
          
          createParagraph('Early warning engagement should begin when reserves fall below five months of imports or spreads exceed 500 basis points. This allows time for program design and negotiations before acute pressure develops. Precautionary credit lines (IMF Flexible Credit Line or Precautionary and Liquidity Line) can provide insurance against market closure. Program request should occur when reserves fall below three months or market access becomes constrained. Crisis response—emergency financing and debt treatment—becomes necessary when markets close and reserves approach depletion.'),
          createParagraph('The key principle is engage before reserves collapse. Countries that approach IFIs while still holding meaningful reserves have negotiating leverage and policy space. Countries that delay until reserves are exhausted must accept whatever terms are available.'),
          
          createHeading2('7.3 Domestic Market Deepening'),
          createParagraph('Deep domestic bond markets provide an alternative to external financing and can reduce currency mismatch risks. Developing these markets requires sustained effort across multiple dimensions: benchmark yield curve construction to provide pricing reference; investor base expansion beyond banks to pension funds, insurance companies, and foreign investors; market-making infrastructure to ensure liquidity; and FX hedging instruments to reduce currency risk premium.'),
          createParagraph('Domestic market development is a medium-term endeavor that cannot address immediate refinancing needs, but it should be pursued in parallel with crisis prevention measures. Countries with deeper domestic markets have more policy space during external stress periods.'),
          
          createHeading2('7.4 Creditor Coordination Framework'),
          createParagraph('When debt treatment becomes necessary, coordinated approaches produce better outcomes than fragmented negotiations. Figure 7.4 presents the creditor coordination framework, emphasizing collective action clauses, comparability of treatment, and transparency.'),
          
          // Add Figure 7.4
          ...createFigure(
            path.join(FIGURES_DIR, 'figure_7_4_creditor_coordination.png'),
            'Figure 7.4: Creditor Coordination Framework',
            'CEDX Framework based on IMF/World Bank standards'
          ),
          
          createParagraph('Collective Action Clauses (CACs) enable majority restructuring that binds all bondholders, preventing holdout problems. Modern CACs include single-limb aggregation that allows treatment across multiple bond series. Countries should ensure all new issuances include state-of-the-art CACs.'),
          createParagraph('Comparability of treatment ensures that official bilateral creditors and private creditors share the burden of adjustment. The Common Framework attempts to operationalize this principle, though implementation challenges persist. Transparency through public debt registries and timely disclosure builds creditor confidence and reduces information asymmetries that impede negotiations.'),
          
          createHeading2('7.5 Implementation Roadmap'),
          createParagraph('Figure 7.3 presents the implementation roadmap for our recommendations, organized by phase and time horizon. Immediate actions (0-6 months) focus on pre-funding facility establishment, IMF/IFI engagement, and debt transparency improvements. Short-term actions (6-24 months) address liability management operations, domestic market development, and FX hedging instruments. Medium-term actions (18-36 months) pursue SOE governance reforms and contingency fund establishment.'),
          
          // Add Figure 7.3
          ...createFigure(
            path.join(FIGURES_DIR, 'figure_7_3_implementation_roadmap.png'),
            'Figure 7.3: Policy Implementation Roadmap',
            'CEDX Implementation Framework'
          ),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // Chapter 8: Execution and Implementation
          createHeading1('Chapter 8. Execution and Implementation Plan'),
          createParagraph('This chapter details the governance structures, resource requirements, and risk management framework for implementing our recommendations.'),
          
          createHeading2('8.1 Delivery Model and Governance'),
          createParagraph('Effective implementation requires clear governance structures with defined roles and accountability. We recommend establishing an inter-agency Debt Management Committee chaired by the Finance Minister with participation from the Central Bank, Debt Management Office, and relevant line ministries. This committee should have authority to approve liability management operations within defined parameters, enabling rapid response to market developments.'),
          createParagraph('Technical implementation capacity should be concentrated in the Debt Management Office, with support from central bank market operations staff. Regular coordination with IFI partners ensures alignment with program requirements. Parliamentary oversight provides democratic accountability for major operations.'),
          
          createHeading2('8.2 Budget and Resource Plan'),
          createParagraph('Implementation costs vary by intervention type. Pre-funding facility setup requires $2-5 billion in committed resources, ideally secured through contingent credit lines rather than drawn borrowing. Liability management operations typically cost $50-100 million in transaction fees, legal costs, and advisory services. Domestic market development costs $10-20 million in infrastructure, capacity building, and technical assistance. FX hedging instrument development costs $5-10 million in infrastructure and regulatory framework development.'),
          createParagraph('Funding sources include: budgetary allocations for operational costs; IFI technical assistance for capacity building; private sector co-investment for market infrastructure; and bilateral support for specific initiatives.'),
          
          createHeading2('8.3 Risk Register and Mitigation'),
          createParagraph('Implementation faces multiple risks that require active management. Figure 8.1 presents the risk heat map for key implementation risks, with mitigation strategies outlined below.'),
          
          // Add Figure 8.1
          ...createFigure(
            path.join(FIGURES_DIR, 'figure_8_1_risk_heat_map.png'),
            'Figure 8.1: Risk Register Heat Map',
            'CEDX Risk Assessment Framework'
          ),
          
          createParagraph('Market risk—spread widening and potential market closure—requires pre-emptive action before thresholds are crossed. Political risk—fiscal policy reversal or IMF program derailment—requires building broad political coalitions and institutional safeguards. Operational risk—debt data gaps or capacity constraints—requires investment in systems and staff. External risk—commodity price shocks or global risk-off events—requires contingency planning and diversified creditor relations.'),
          
          createHeading2('8.4 Monitoring and Learning'),
          createParagraph('Continuous monitoring enables adaptive management as conditions evolve. Key performance indicators should include: reserve coverage in months of imports; spread levels and trends; bid-to-cover ratios in debt auctions; debt service to revenue ratio; and GFN trajectory. Monthly dashboards should track these indicators against thresholds, with escalation protocols when warning signs emerge.'),
          createParagraph('Learning from implementation should be systematically captured and incorporated into subsequent operations. After-action reviews of liability management operations, annual assessments of debt management capacity, and regular benchmarking against international best practices support continuous improvement.'),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // Chapter 9: MEL
          createHeading1('Chapter 9. Monitoring, Evaluation, and Learning'),
          createParagraph('This chapter establishes the framework for tracking implementation progress, evaluating outcomes, and incorporating lessons learned into ongoing practice.'),
          
          createHeading2('9.1 Results Framework'),
          createParagraph('The results framework connects inputs and activities to outputs, outcomes, and impact. At the impact level, the goal is sovereign debt sustainability and avoidance of disorderly default. Outcomes include maintained market access, reduced refinancing concentration, and enhanced fiscal space. Outputs include completed liability management operations, established contingent facilities, and deepened domestic markets. Activities encompass the specific interventions recommended in this report.'),
          createParagraph('Assumptions underlying the results framework include: continued IFI support for implementing countries; no major external shock that overwhelms preventive measures; sufficient political will to implement reforms; and accurate data for monitoring and decision-making.'),
          
          createHeading2('9.2 Indicator Definitions'),
          createParagraph('Key performance indicators should be defined with specific formulas, baselines, targets, data sources, and reporting frequencies. For each country, we recommend tracking: Reserve coverage (months of imports) with weekly reporting during acute stress; Sovereign spread (basis points) with daily market monitoring; Debt service to revenue ratio with quarterly reporting; GFN trajectory with annual projections; and Bid-to-cover ratio for debt auctions as an indicator of market confidence.'),
          createParagraph('Targets should be set relative to baseline values and threshold levels. For example, countries with reserve coverage below three months should target reaching the minimum threshold within six months and five months within eighteen months.'),
          
          createHeading2('9.3 Learning and Adaptation'),
          createParagraph('Effective implementation requires learning from both successes and failures. We recommend establishing formal learning processes including: quarterly implementation reviews to assess progress and identify obstacles; after-action reviews following major operations; peer learning exchanges with other sovereigns; and integration of academic research into operational practice.'),
          createParagraph('Learning questions to guide ongoing inquiry include: What factors enable successful preventive liability management? How do political economy constraints interact with technical solutions? What early warning indicators prove most predictive of refinancing distress? How can international coordination be improved for future cases?'),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // Chapter 10: Conclusion
          createHeading1('Chapter 10. Conclusion'),
          createParagraph('The 2026 refinancing wall represents a systemic risk to global financial stability and development progress. Our analysis has identified the countries facing the greatest vulnerability, quantified the financing gaps they confront, and specified the policy interventions that can prevent crisis. The findings are sobering but actionable.'),
          
          createHeading2('10.1 Overall Conclusion'),
          createParagraph('The refinancing wall is fundamentally a timing problem—debt maturing when refinancing conditions are unfavorable and alternatives are limited. Countries with seemingly sustainable aggregate debt positions face acute rollover crises when maturities bunch, markets close, and reserves prove inadequate. The key to prevention is early identification of vulnerabilities and proactive intervention before options narrow.'),
          createParagraph('Our quantitative analysis reveals significant financing gaps across our sample countries, particularly under stress scenarios. Pakistan, Ghana, and Egypt face the largest absolute gaps, while Sri Lanka and Zambia confront the most constrained capacity to bridge them. These gaps cannot be closed through market financing alone—IFI support, bilateral assistance, and in some cases debt treatment will be necessary.'),
          createParagraph('The case studies demonstrate that early engagement with creditors and IFIs produces better outcomes than delayed action. Countries that implemented preventive liability management or secured precautionary credit lines navigated the challenging 2022-2024 period more successfully than those that delayed until markets closed. This pattern holds across diverse country contexts and should inform future policy design.'),
          
          createHeading2('10.2 Immediate Next Steps'),
          createParagraph('For policymakers in vulnerable countries, the immediate priority is establishing pre-funding facilities before reserves drop below critical thresholds. This requires engagement with IFIs on contingent credit lines, assessment of liability management options, and development of domestic financing capacity. Governments should establish or strengthen inter-agency coordination mechanisms for debt management and ensure adequate technical capacity in debt offices.'),
          createParagraph('For IFIs and bilateral partners, the priority is providing timely support that prevents crisis rather than responding after the fact. This means expediting precautionary facility approvals, enhancing early warning systems, and developing rapid-response financing instruments. The cost of prevention is far lower than the cost of crisis response.'),
          createParagraph('For private creditors, the priority is engaging constructively with preventive liability management operations rather than waiting for distressed restructuring. Early exchanges and extensions typically provide better recovery values than post-default negotiations, while avoiding the economic disruption that crisis imposes on debtor countries.'),
          
          createHeading2('10.3 Open Questions'),
          createParagraph('Several questions remain for future research. How will the evolving creditor landscape—with China and other non-traditional lenders playing larger roles—affect the dynamics of debt treatment? Can early warning systems be improved to provide more precise signals of approaching crisis? What governance reforms most effectively prevent the political economy failures that often underlie debt distress? Addressing these questions will strengthen the framework for managing the ongoing refinancing challenges that will persist beyond the 2026 maturity wall.'),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // References
          createHeading1('References'),
          createParagraph('Asonuma, T., & Trebesch, C. (2016). Sovereign debt restructurings: Precedents and outcomes. Journal of the European Economic Association, 14(1), 173-214.'),
          createParagraph('Arellano, C. (2008). Default risk and income fluctuations in emerging economies. American Economic Review, 98(3), 690-712.'),
          createParagraph('Bianchi, J., Hatchondo, J. C., & Martinez, L. (2018). International reserves and rollover risk. American Economic Review, 108(9), 2629-2670.'),
          createParagraph('Borensztein, E., Cowan, K., & Valenzuela, P. (2013). Sovereign ceilings "lite"? The impact of sovereign ratings on corporate ratings in emerging market economies. Journal of Banking & Finance, 37(11), 4014-4024.'),
          createParagraph('Broner, F. A., Gelos, R. G., & Martin, R. (2006). Sovereign debt maturity structure. Unpublished manuscript, Inter-American Development Bank.'),
          createParagraph('Calvo, G. A. (1988). Servicing the public debt: The role of expectations. American Economic Review, 78(4), 647-661.'),
          createParagraph('Calvo, G. A., & Mendoza, E. G. (2000). Rational contagion and the globalization of securities markets. Journal of International Economics, 51(1), 79-113.'),
          createParagraph('Chamon, M. (2007). Can debt relief cause a debt crisis? The World Bank Economic Review, 21(2), 229-248.'),
          createParagraph('Cruces, J. J., & Trebesch, C. (2013). Sovereign defaults: The price of haircuts. American Economic Journal: Macroeconomics, 5(3), 85-117.'),
          createParagraph('Diaz-Cassou, J., Erce-Domínguez, A., & Vázquez-Zamora, J. J. (2008). Recent episodes of sovereign debt restructurings: A case-study approach. Banco de España Occasional Paper No. 0804.'),
          createParagraph('Eaton, J., & Gersovitz, M. (1981). Debt with potential repudiation: Theoretical and empirical analysis. Review of Economic Studies, 48(2), 289-309.'),
          createParagraph('Gelos, R. G., Sahay, R., & Sandleris, G. (2011). Sovereign borrowing by emerging markets: A case study of Peru. Journal of International Money and Finance, 30(5), 989-1007.'),
          createParagraph('Ghosh, A. R., Ostry, J. D., & Tsangarides, C. G. (2017). Shifting motives: Explaining the buildup in official reserves in emerging markets since the 1980s. IMF Economic Review, 65(2), 328-363.'),
          createParagraph('Hatchondo, J. C., & Martinez, L. (2009). Long-duration bonds and sovereign defaults. Journal of International Economics, 79(1), 117-125.'),
          createParagraph('International Monetary Fund. (2024). World Economic Outlook: October 2024. Washington, DC: IMF.'),
          createParagraph('International Monetary Fund. (2024). Ghana: Staff Report for the 2024 Article IV Consultation and Third Review. IMF Country Report No. 24/XXX.'),
          createParagraph('International Monetary Fund. (2023). Sri Lanka: Staff Report for the 2023 Article IV Consultation and First Review. IMF Country Report No. 23/XXX.'),
          createParagraph('International Monetary Fund. (2024). Zambia: Staff Report for the 2024 Article IV Consultation. IMF Country Report No. 24/XXX.'),
          createParagraph('International Monetary Fund. (2024). Pakistan: Staff Report for the 2024 Article IV Consultation. IMF Country Report No. 24/XXX.'),
          createParagraph('Jeanne, O., & Rancière, R. (2011). The optimal level of international reserves for emerging market countries: A new formula and some applications. Economic Journal, 121(555), 905-930.'),
          createParagraph('Kohlscheen, E., & O\'Connell, S. A. (2020). Sovereign default and the stability of the banking system. Journal of International Money and Finance, 102, 102108.'),
          createParagraph('Meyer, J., Reinhart, C. M., & Trebesch, C. (2022). Sovereign bonds since Waterloo. Quarterly Journal of Economics, 137(3), 1615-1680.'),
          createParagraph('Obstfeld, M. (1996). Models of currency crises with self-fulfilling features. European Economic Review, 40(3-5), 1037-1047.'),
          createParagraph('Panizza, U., Sturzenegger, F., & Zettelmeyer, J. (2009). The economics and law of sovereign debt and default. Journal of Economic Literature, 47(3), 651-698.'),
          createParagraph('Reinhart, C. M., & Rogoff, K. S. (2009). This Time Is Different: Eight Centuries of Financial Folly. Princeton University Press.'),
          createParagraph('Reinhart, C. M., & Rogoff, K. S. (2011). From financial crash to debt crisis. American Economic Review, 101(5), 1676-1706.'),
          createParagraph('Schmitt-Grohé, S., & Uribe, M. (2017). Is optimal capital control policy countercyclical? Journal of International Economics, 108, 345-361.'),
          createParagraph('Sturzenegger, F., & Zettelmeyer, J. (2006). Debt Defaults and Lessons from a Decade of Crises. MIT Press.'),
          createParagraph('Tomz, M., & Wright, M. L. (2013). Empirical research on sovereign debt and default. Annual Review of Economics, 5, 247-278.'),
          createParagraph('Trebesch, C. (2009). The cost of aggressive sovereign debt policies: How much is the private sector affected? IMF Working Paper No. 09/29.'),
          createParagraph('World Bank. (2024). International Debt Statistics 2024. Washington, DC: World Bank.'),
          createParagraph('World Bank. (2024). Global Economic Prospects: January 2024. Washington, DC: World Bank.'),
          createParagraph('Wright, M. L. (2012). The crisis of sovereign debt. Annual Review of Economics, 4, 307-332.'),
          
          new Paragraph({ children: [new PageBreak()] }),
          
          // Appendix
          createHeading1('Appendix A. Detailed Methodology'),
          createParagraph('This appendix provides additional details on the analytical methods employed in this report.'),
          createHeading2('A.1 Gross Financing Need Calculation'),
          createParagraph('Gross Financing Need (GFN) is calculated using the standard IMF formula: GFN = Amortization + Interest Payments + Primary Deficit. Amortization includes all debt principal repayments due in the relevant year. Interest payments include coupon payments on all outstanding debt. The primary deficit is the difference between government expenditure (excluding interest) and government revenue.'),
          createParagraph('For external debt, we convert all obligations to USD equivalents using end-period exchange rates. For local currency debt, we present both local currency values and USD equivalents. Contingent liabilities are not included in baseline GFN but are discussed qualitatively.'),
          createHeading2('A.2 Stress Scenario Construction'),
          createParagraph('Stress scenarios apply uniform shocks across countries: +300 basis points spread widening (reflecting typical risk-off episodes); 15 percent currency depreciation (reflecting typical emerging market FX stress); 1.5 percentage point growth shortfall (reflecting output gap during debt distress). These shocks are applied to the baseline projections to generate stress scenario outcomes.'),
          createHeading2('A.3 Refinancing Gap Model'),
          createParagraph('The refinancing gap model compares financing needs against available resources. Available resources include: Market access (estimated from recent issuance patterns and current spread levels); Reserve drawdown (limited to maintain minimum coverage); IFI support (based on current or anticipated program arrangements); Other sources (bilateral support, privatization proceeds, etc.). The gap is calculated as: Gap = GFN - Available Resources.'),
          
          createHeading1('Appendix B. Supplementary Data Tables'),
          createParagraph('Supplementary data tables are available in the accompanying data files. Table B.1 provides detailed maturity profiles by country and instrument. Table B.2 provides historical spread data. Table B.3 provides reserve adequacy indicators. Table B.4 provides debt service projections.'),
          
          createHeading1('Appendix C. Glossary'),
          createParagraph('Basis Point (bp): One hundredth of one percentage point (0.01%).'),
          createParagraph('Collective Action Clause (CAC): Bond provision allowing a qualified majority of bondholders to bind all bondholders to a restructuring.'),
          createParagraph('Common Framework: G20 initiative for coordinated sovereign debt treatment across creditor classes.'),
          createParagraph('Debt Service: Total payments due on debt, including interest and principal.'),
          createParagraph('Eurobond: International bond denominated in a currency different from the issuer\'s domestic currency.'),
          createParagraph('Gross Financing Need (GFN): Total annual financing requirement including amortization, interest, and primary deficit.'),
          createParagraph('Net Present Value (NPV): Current value of future cash flows discounted at an appropriate rate.'),
          createParagraph('Sovereign Spread: Yield differential between a sovereign bond and a benchmark (typically US Treasuries).'),
          createParagraph('State-Owned Enterprise (SOE): Government-owned corporation that may carry contingent liabilities for the sovereign.'),
        ]
      }
    ]
  });

  // Generate and save document
  console.log('Generating document buffer...');
  const buffer = await Packer.toBuffer(doc);
  const outputPath = path.join(OUTPUT_DIR, 'The_2026_Refinancing_Wall_Report.docx');
  fs.writeFileSync(outputPath, buffer);
  console.log(`Document saved to: ${outputPath}`);
  return outputPath;
}

// Execute
generateDocument()
  .then(path => console.log('Success:', path))
  .catch(err => console.error('Error:', err));
