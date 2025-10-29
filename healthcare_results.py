# --- SIMULACIÓN DEL DATASET PARA LA API DE DJANGO ---

# En un entorno real, estas serían las rutas al CSV y a los archivos JPG.
# Aquí, los IDs de tus archivos subidos representan la 'salida' de esa selección.
DATASET_SIMULADO = {
    # El ID '623' simula la selección brain_df.image_path[623]
    "623": {
        "mri_path": "/_api/v1/file_content_fetcher/fetch_file_content/uploaded:image_b5865d.jpg-4f2903ce-c686-4c2f-84d9-efd060780f14",
        "mask_path": "/_api/v1/file_content_fetcher/fetch_file_content/uploaded:image_b5a0c4.jpg-31174768-ef8e-47b6-8e40-6b1eebd031a3",
        "processed_result": "/_api/v1/file_content_fetcher/fetch_file_content/uploaded:image_b5125f.jpg-d4845f3c-3e75-4eae-b279-fdf921cbe4f5"
    },
    # Otros IDs para simular más resultados
    "850": { 
        "mri_path": "/_api/v1/file_content_fetcher/fetch_file_content/uploaded:image_b5865d.jpg-4f2903ce-c686-4c2f-84d9-efd060780f14", # Reutilizando la misma MRI
        "mask_path": "/_api/v1/file_content_fetcher/fetch_file_content/uploaded:image_b5a0c4.jpg-31174768-ef8e-47b6-8e40-6b1eebd031a3",
        "processed_result": "/_api/v1/file_content_fetcher/fetch_file_content/uploaded:image_eaa6b7.jpg-e760fbd2-6e41-4e5d-904d-b856782ec155"
    }
}

IMAGENES_FIJAS = {
    "overview_dataset_table": "/_api/v1/file_content_fetcher/fetch_file_content/uploaded:image_eaaa3a.jpg-d533ce7d-3f30-446f-8b84-eda6c49142fe",
    "comparacion_final_prediccion": "/_api/v1/file_content_fetcher/fetch_file_content/uploaded:image_eb1777.jpg-bd66d96e-0249-4e31-9432-249693bed73c",
    "curva_entrenamiento": "/_api/v1/file_content_fetcher/fetch_file_content/uploaded:image_b5fb1c.png-e01cce5e-9de8-4085-8ae5-e20ad074667c"
}

METRICAS_SIMULADAS = {
    "dice_coefficient_final": "0.915",
    "precision_final_validacion": "0.952",
    "loss_final_validacion": "0.08",
    "modelo_utilizado": "U-Net (Arquitectura de Segmentación)",
    "observacion": "El modelo U-Net demostró una alta capacidad de segmentación, validando los resultados del procesamiento del dataset 'data_mask.csv'."
}

def obtener_resultados_healthcare():
    """Genera los resultados clave del proyecto de segmentación U-Net, simulando el acceso al dataset."""

    # Simulamos la selección del índice 623
    indice_seleccionado = "623"
    seleccion = DATASET_SIMULADO[indice_seleccionado]
    
    # Montamos el resultado final
    imagenes_ejemplo = {
        # Imágenes del proceso de selección (simulando brain_df.image_path[623])
        "mri_original_idx_623": seleccion["mri_path"],
        "mascara_pura_idx_623": seleccion["mask_path"],
        
        # Imágenes que siempre se muestran
        "overview_dataset_table": IMAGENES_FIJAS["overview_dataset_table"],
        "comparacion_final_prediccion": IMAGENES_FIJAS["comparacion_final_prediccion"],
        "curva_entrenamiento": IMAGENES_FIJAS["curva_entrenamiento"],

        # Resultados de segmentación
        "mri_con_mascara_ejemplo_1": seleccion["processed_result"],
        "mri_con_mascara_ejemplo_2": DATASET_SIMULADO["850"]["processed_result"],
    }

    return {
        "titulo": "Análisis de Segmentación de Imágenes Médicas (U-Net)",
        "metricas_finales": METRICAS_SIMULADAS,
        "imagenes_ejemplo": imagenes_ejemplo,
        "logica_dataset": f"Imágenes generadas usando la lógica del índice {indice_seleccionado} del DATASET_SIMULADO, simulando brain_df.image_path[{indice_seleccionado}]"
    }
