import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime
import os

# Use Agg backend for non-interactive plotting
matplotlib.use('Agg')

class StatisticsGraphs:
    """Generate statistics graphs using matplotlib"""

    @staticmethod
    def create_graphs_directory():
        """Create graphs directory if it doesn't exist"""
        if not os.path.exists("graphs"):
            os.makedirs("graphs")
        return "graphs"

    @staticmethod
    def generate_bed_status_pie_chart(total_beds, occupied_beds, available_beds):
        """Generate pie chart for bed status"""
        try:
            graphs_dir = StatisticsGraphs.create_graphs_directory()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(graphs_dir, f"bed_status_pie_{timestamp}.png")

            fig, ax = plt.subplots(figsize=(8, 6))
            sizes = [occupied_beds, available_beds]
            labels = [f'Occupied ({occupied_beds})', f'Available ({available_beds})']
            colors = ['#ff6b6b', '#51cf66']
            explode = (0.05, 0)

            ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                   shadow=True, startangle=90, textprops={'fontsize': 12, 'weight': 'bold'})
            ax.set_title('Bed Status Distribution', fontsize=14, weight='bold', pad=20)

            plt.tight_layout()
            plt.savefig(filename, dpi=100, bbox_inches='tight')
            plt.close()

            print(f"[v0] Bed status pie chart saved to {filename}")
            return filename
        except Exception as e:
            print(f"[v0] Error generating bed status pie chart: {e}")
            raise

    @staticmethod
    def generate_alos_bar_chart(alos_data):
        """Generate bar chart for ALOS by bed type"""
        try:
            graphs_dir = StatisticsGraphs.create_graphs_directory()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(graphs_dir, f"alos_bar_{timestamp}.png")

            bed_types = [row['bed_type'] for row in alos_data]
            alos_values = [float(row['average_los']) if row['average_los'] else 0 for row in alos_data]

            fig, ax = plt.subplots(figsize=(10, 6))
            bars = ax.bar(bed_types, alos_values, color=['#4c6ef5', '#15aabf', '#fd7e14'], edgecolor='black', linewidth=1.5)

            # Add value labels on bars
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{height:.2f}',
                       ha='center', va='bottom', fontsize=11, weight='bold')

            ax.set_xlabel('Bed Type', fontsize=12, weight='bold')
            ax.set_ylabel('Average Length of Stay (days)', fontsize=12, weight='bold')
            ax.set_title('Average Length of Stay by Bed Type', fontsize=14, weight='bold', pad=20)
            ax.grid(axis='y', alpha=0.3, linestyle='--')

            plt.tight_layout()
            plt.savefig(filename, dpi=100, bbox_inches='tight')
            plt.close()

            print(f"[v0] ALOS bar chart saved to {filename}")
            return filename
        except Exception as e:
            print(f"[v0] Error generating ALOS bar chart: {e}")
            raise

    @staticmethod
    def generate_admissions_trend_chart(admissions_by_date):
        """Generate line chart for admissions trend"""
        try:
            graphs_dir = StatisticsGraphs.create_graphs_directory()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(graphs_dir, f"admissions_trend_{timestamp}.png")

            dates = [row['date'] for row in admissions_by_date]
            counts = [row['count'] for row in admissions_by_date]

            fig, ax = plt.subplots(figsize=(12, 6))
            ax.plot(dates, counts, marker='o', linewidth=2.5, markersize=8, color='#4c6ef5', label='Admissions')
            ax.fill_between(range(len(dates)), counts, alpha=0.3, color='#4c6ef5')

            ax.set_xlabel('Date', fontsize=12, weight='bold')
            ax.set_ylabel('Number of Admissions', fontsize=12, weight='bold')
            ax.set_title('Admissions Trend Over Time', fontsize=14, weight='bold', pad=20)
            ax.grid(True, alpha=0.3, linestyle='--')
            ax.legend(fontsize=11)

            # Rotate x-axis labels for better readability
            plt.xticks(rotation=45, ha='right')

            plt.tight_layout()
            plt.savefig(filename, dpi=100, bbox_inches='tight')
            plt.close()

            print(f"[v0] Admissions trend chart saved to {filename}")
            return filename
        except Exception as e:
            print(f"[v0] Error generating admissions trend chart: {e}")
            raise

    @staticmethod
    def generate_bed_type_distribution_chart(bed_type_data):
        """Generate bar chart for bed type distribution"""
        try:
            graphs_dir = StatisticsGraphs.create_graphs_directory()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(graphs_dir, f"bed_type_distribution_{timestamp}.png")

            bed_types = [row['bed_type'] for row in bed_type_data]
            counts = [row['count'] for row in bed_type_data]

            fig, ax = plt.subplots(figsize=(10, 6))
            bars = ax.bar(bed_types, counts, color=['#4c6ef5', '#15aabf', '#fd7e14'], edgecolor='black', linewidth=1.5)

            # Add value labels on bars
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{int(height)}',
                       ha='center', va='bottom', fontsize=11, weight='bold')

            ax.set_xlabel('Bed Type', fontsize=12, weight='bold')
            ax.set_ylabel('Number of Beds', fontsize=12, weight='bold')
            ax.set_title('Bed Distribution by Type', fontsize=14, weight='bold', pad=20)
            ax.grid(axis='y', alpha=0.3, linestyle='--')

            plt.tight_layout()
            plt.savefig(filename, dpi=100, bbox_inches='tight')
            plt.close()

            print(f"[v0] Bed type distribution chart saved to {filename}")
            return filename
        except Exception as e:
            print(f"[v0] Error generating bed type distribution chart: {e}")
            raise
