📘 Power BI Notes (Part 1)
Based on Our Training
📅 Day 1
What is Power BI?

Power BI is a Business Intelligence (BI) and Data Visualization tool developed by Microsoft. It helps convert raw data into interactive reports and dashboards for better decision-making.

Why Use Power BI?
Analyze large amounts of data.
Create interactive dashboards.
Generate business insights.
Connect multiple data sources.
Share reports with others.
Components of Power BI
Power BI Desktop
Power BI Service
Power BI Mobile
Power BI Gateway
Power BI Report Server
Power BI Views
1. Report View
Create reports and dashboards.
Add charts and visuals.
Format visuals.
2. Data View
View imported data.
Create calculated columns.
Check data types.
3. Model View
Create relationships.
Manage tables.
Build data models.
Data Sources

Power BI can import data from:

Excel
CSV
SQL Server
MySQL
Oracle
Web
SharePoint
Azure
Data Modeling
Star Schema ⭐

Contains:

One Fact Table
Multiple Dimension Tables

Advantages

Fast
Easy
Best Performance

Example

          Product
             |
Customer — Sales — Date
             |
          Region
Snowflake Schema

Dimension tables are normalized into multiple tables.

Advantages

Less redundancy
Better normalization

Disadvantages

Complex
Slower than Star Schema
DAX

DAX = Data Analysis Expressions

Used for:

Calculations
Measures
Calculated Columns
Types of DAX
1. Implicit Measure

Automatically created by Power BI.

Example:

Sum of Sales
Average Profit
2. Explicit Measure

Created by the user.

Example

Total Sales = SUM(Orders[Sales])
Measure vs Calculated Column
Measure	Calculated Column
Calculated on demand	Stored in table
Less memory	More memory
Used in visuals	Used row by row
Dashboard Design Workflow
Import Data
      ↓
Clean Data
      ↓
Create Relationships
      ↓
Create Measures
      ↓
Build Visuals
      ↓
Format Dashboard
      ↓
Business Insights
Dashboard We Built
KPI Cards
Total Sales
Total Profit
Total Orders
Total Quantity
Charts
Clustered Bar Chart
Area Chart
Donut Chart
Scatter Chart
Map
Table
Clustered Column Chart
Slicers
Visual 1
Clustered Bar Chart
Business Question

Which category generates the highest sales?

Fields

Y-axis → Category

X-axis → Total Sales

Why?

Best for comparing categories.

Visual 2
Area Chart
Business Question

How have sales changed over time?

Fields

X-axis → Order Date (Month)

Y-axis → Total Sales

Why?

Shows trends over time.

Visual 3
Donut Chart
Business Question

Which region contributes the highest percentage of sales?

Fields

Legend → Region

Values → Total Sales

Why?

Shows percentage contribution.

Visual 4
Scatter Chart
Business Question

Does higher sales always lead to higher profit?

Fields

X-axis → Sales

Y-axis → Profit

Legend → Product Name

Why?

Shows relationship between two numerical variables.

Visual 5
Map
Business Question

Which countries generate the highest sales?

Fields

Location → Country

Bubble Size → Total Sales

Tooltips → Total Profit

Why?

Shows geographical distribution.

Visual 6
Table
Business Question

Which products generate the highest sales?

Fields
Product Name
Category
Total Sales
Total Profit
Total Quantity

Filter

Top N = 10

Why?

Shows exact values.

Visual 7
Clustered Column Chart
Business Question

Which shipping mode generates the highest sales?

Fields

X-axis → Ship Mode

Y-axis → Total Sales

Why?

Best for comparing categories vertically.

Visual 8
Slicer
Business Question

How can users interactively filter the dashboard?

Used:

Year
Region
Category
Segment
Ship Mode
Dashboard Principles
Structure first
Data second
Formatting third
Colors last
Professional Dashboard Rules
Keep equal spacing.
Use consistent colors.
Don't overcrowd visuals.
Every chart should answer one business question.
Use slicers for interaction.
Power BI Concepts Learned
KPI

Key Performance Indicator.

Measures business performance.

Dashboard

Collection of visuals on one page.

Measure

Dynamic calculation using DAX.

Slicer

Interactive filter.

Cross Filtering

Selecting one visual filters other visuals automatically.

Hierarchy

Example

Market
   ↓
Region
   ↓
Country
   ↓
State
   ↓
City
Aggregation

Combining multiple rows into one value.

Example

100
200
300

SUM = 600
Correlation

Relationship between two variables.

Example

Sales ↑

Profit ↑

Outlier

A value that is very different from the rest.

Geospatial Analysis

Analysis based on location.

Example

Sales by Country

Visual Cue

Using colors and icons to improve understanding.

Example

💰 Sales

📈 Profit

📦 Orders

🛒 Quantity

Word of the Day (Collected)
KPI
Dashboard
Measure
Slicer
Hierarchy
Aggregation
Correlation
Outlier
Geospatial Analysis
Visual Cue
Top N Filter
Ranking
Interview Questions
Why Bar Chart?

Best for comparing categories.

Why Area Chart?

Best for trends over time.

Why Donut Chart?

Best for percentage contribution.

Why Scatter Chart?

Shows relationship between two numerical variables.

Why Map?

Shows geographical analysis.

Why Table?

Shows exact values.

Why Column Chart?

Best for comparing categorical values vertically.

Why Slicer?

Makes the dashboard interactive.

Mentor Tips ⭐
Think like a business analyst, not just a Power BI user.
Ask "What business question am I answering?" before choosing a visual.
Use measures instead of raw columns whenever appropriate.
Build the layout first, then connect data, then format.
Keep dashboards clean, consistent, and easy to understand.
📚 Word of the Day

Business Insight

A meaningful conclusion drawn from data that helps an organization make better decisions.

Example:

"Technology has the highest sales, but some products have low profit due to discounts."

These notes cover everything we've learned so far and are ideal for quick revision before class, interviews, or practical exams.