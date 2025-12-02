# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import pandas as pd
import matplotlib.pyplot as plt
import os


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    
    # Crear la carpeta docs si no existe
    os.makedirs("docs", exist_ok=True)

    # Leer los datos
    df = pd.read_csv("files/input/shipping-data.csv")

    # Configurar el estilo general de matplotlib
    plt.style.use("default")


    fig1, ax1 = plt.subplots(figsize=(6, 4))
    warehouse_counts = df["Warehouse_block"].value_counts().sort_index()
    
    ax1.bar(
        warehouse_counts.index,
        warehouse_counts.values,
        color="tab:blue",
        edgecolor="black"
    )
    ax1.set_xlabel("Warehouse Block", fontsize=10)
    ax1.set_ylabel("Count", fontsize=10)
    ax1.set_title("Warehouse Block Distribution", fontsize=12, fontweight="bold")
    ax1.grid(axis="y", alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("docs/shipping_per_warehouse.png", dpi=100, bbox_inches="tight")
    plt.close()

 
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    shipment_counts = df["Mode_of_Shipment"].value_counts()
    
    ax2.bar(
        shipment_counts.index,
        shipment_counts.values,
        color="tab:orange",
        edgecolor="black"
    )
    ax2.set_xlabel("Mode of Shipment", fontsize=10)
    ax2.set_ylabel("Count", fontsize=10)
    ax2.set_title("Mode of Shipment Distribution", fontsize=12, fontweight="bold")
    ax2.grid(axis="y", alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("docs/mode_of_shipment.png", dpi=100, bbox_inches="tight")
    plt.close()


    fig3, ax3 = plt.subplots(figsize=(6, 4))
    
    ax3.hist(
        df["Customer_rating"],
        bins=5,
        color="tab:green",
        edgecolor="black",
        alpha=0.7
    )
    ax3.set_xlabel("Customer Rating", fontsize=10)
    ax3.set_ylabel("Frequency", fontsize=10)
    ax3.set_title("Customer Rating Distribution", fontsize=12, fontweight="bold")
    ax3.grid(axis="y", alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("docs/average_customer_rating.png", dpi=100, bbox_inches="tight")
    plt.close()

    fig4, ax4 = plt.subplots(figsize=(6, 4))
    
    ax4.hist(
        df["Weight_in_gms"],
        bins=30,
        color="tab:red",
        edgecolor="black",
        alpha=0.7
    )
    ax4.set_xlabel("Weight (grams)", fontsize=10)
    ax4.set_ylabel("Frequency", fontsize=10)
    ax4.set_title("Weight Distribution", fontsize=12, fontweight="bold")
    ax4.grid(axis="y", alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("docs/weight_distribution.png", dpi=100, bbox_inches="tight")
    plt.close()

  
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shipping Data Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
        }
        
        .dashboard {
            max-width: 1400px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }
        
        .chart-container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .chart-container img {
            width: 100%;
            height: auto;
            display: block;
        }
        
        @media (max-width: 768px) {
            .dashboard {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <h1>Shipping Data Dashboard</h1>
    
    <div class="dashboard">
        <div class="chart-container">
            <img src="shipping_per_warehouse.png" alt="Warehouse Block Distribution">
        </div>
        
        <div class="chart-container">
            <img src="mode_of_shipment.png" alt="Mode of Shipment Distribution">
        </div>
        
        <div class="chart-container">
            <img src="average_customer_rating.png" alt="Customer Rating Distribution">
        </div>
        
        <div class="chart-container">
            <img src="weight_distribution.png" alt="Weight Distribution">
        </div>
    </div>
</body>
</html>
"""

    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    
    
    
    
