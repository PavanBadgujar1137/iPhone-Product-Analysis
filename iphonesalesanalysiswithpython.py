import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset
data = pd.read_csv("apple_products.csv")

# Filter and sort the top 10 highest-rated iPhone products
highest_rated = data.sort_values(by="Star Rating", ascending=False).head(10)

# Extract product names and number of ratings
product_counts = highest_rated['Product Name'].value_counts()
labels = product_counts.index
ratings = highest_rated["Number Of Ratings"]

# Plot bar chart for the number of ratings of the top-rated iPhones with custom styling
figure = px.bar(
    highest_rated, 
    x=labels, 
    y=ratings, 
    title="Number of Ratings of Highest Rated iPhones",
    color=labels,  # Different colors for each iPhone
    text=ratings,  # Display ratings on top of bars
)

# Customize layout with borders, fonts, and background color
figure.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
    paper_bgcolor='rgba(245, 246, 249, 1)',  # Light grey background for the plot
    font=dict(family="Arial", size=14, color="RebeccaPurple"),
    title_font=dict(size=24, color='DarkBlue', family="Arial Black"),
    xaxis=dict(showline=True, linewidth=2, linecolor='black', mirror=True),
    yaxis=dict(showline=True, linewidth=2, linecolor='black', mirror=True),
    hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell"),
    margin=dict(l=40, r=40, t=40, b=40),  # Adjust margins for better visibility
    title_x=0.5  # Center the title
)
figure.show()

# Extract product names and number of reviews
reviews = highest_rated["Number Of Reviews"]

# Plot bar chart for the number of reviews of the top-rated iPhones with custom styling
figure = px.bar(
    highest_rated, 
    x=labels, 
    y=reviews, 
    title="Number of Reviews of Highest Rated iPhones",
    color=labels,  # Different colors for each iPhone
    text=reviews,  # Display reviews on top of bars
)

# Customize layout
figure.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(245, 246, 249, 1)',
    font=dict(family="Arial", size=14, color="RebeccaPurple"),
    title_font=dict(size=24, color='DarkBlue', family="Arial Black"),
    xaxis=dict(showline=True, linewidth=2, linecolor='black', mirror=True),
    yaxis=dict(showline=True, linewidth=2, linecolor='black', mirror=True),
    hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell"),
    margin=dict(l=40, r=40, t=40, b=40),
    title_x=0.5
)
figure.show()

# Scatter plot to show the relationship between sale price and number of ratings with custom styling
figure = px.scatter(
    data_frame=data, 
    x="Number Of Ratings", 
    y="Sale Price", 
    size="Discount Percentage", 
    color="Product Name",  # Color by product name
    trendline="ols", 
    title="Relationship between Sale Price and Number of Ratings of iPhones",
    template="plotly_dark"  # Dark theme for contrast
)

# Customize layout
figure.update_layout(
    font=dict(family="Arial", size=14, color="white"),
    title_font=dict(size=24, color='LightBlue', family="Arial Black"),
    hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell"),
    title_x=0.5
)
figure.show()

# Scatter plot to show the relationship between discount percentage and number of ratings with custom styling
figure = px.scatter(
    data_frame=data, 
    x="Number Of Ratings", 
    y="Discount Percentage", 
    size="Sale Price", 
    color="Product Name",  # Color by product name
    trendline="ols", 
    title="Relationship between Discount Percentage and Number of Ratings of iPhones",
    template="plotly_dark"  # Dark theme for contrast
)

# Customize layout
figure.update_layout(
    font=dict(family="Arial", size=14, color="white"),
    title_font=dict(size=24, color='LightBlue', family="Arial Black"),
    hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell"),
    title_x=0.5
)
figure.show()
