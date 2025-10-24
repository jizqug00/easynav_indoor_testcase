# 🏠 EasyNav Indoor Testcase

Este paquete contiene las herramientas, un conjunto de **mapas, parámetros y lanzadores**, para probar el framework [EasyNavigation](https://github.com/jizqug00/EasyNavigation.git) en entornos **indoor 2D** simulados.

Incluye configuraciones listas para usar con **costmaps**, **mapas simples**, y entornos multirrobot, además de archivos RViz para visualización.  

Los **ejemplos prácticos de mapping y navegación 2D** se encuentran en la documentación oficial:  
👉 [https://easynavigation.github.io/howtos](https://easynavigation.github.io/howtos)

---

## 📦 Contenido del paquete

easynav_indoor_testcase/
├── launch/
│   └── easynav_multirobot.launch.py     # Lanzador para pruebas multirrobot
├── maps/
│   ├── default.map                      # Mapa de referencia
│   ├── home.map                         # Otro mapa de ejemplo
│   ├── home2.{pgm,yaml}                 # Mapa 'home2' con su metadata
│   ├── warehouse.{pgm,yaml}             # Mapa 'warehouse' con su metadata
├── robots_params/
│   ├── costmap.params.yaml              # Parámetros estándar de costmap
│   ├── costmap.mapping.params.yaml      # Parámetros de costmap para mapeo
│   ├── costmap.serest.params.yaml       # Costmap para escenarios 'serest'
│   ├── costmap_multirobot.params.yaml   # Configuración de costmap multirrobot
│   ├── dummy.params.yaml                # Parámetros genéricos de ejemplo
│   ├── simple.params.yaml               # Parámetros simples de navegación
│   └── simple.mapping.params.yaml       # Parámetros simples de mapeo
├── rviz/
│   └── simple.rviz                      # Configuración RViz para visualización
├── CMakeLists.txt
├── package.xml
└── LICENSE

---

## 🚀 Instalación

Clona el repositorio dentro de tu *workspace* de ROS 2 (por ejemplo, `easynav_ws/src`):

    cd ~/easynav_ws/src
    git clone https://github.com/jizqug00/easynav_indoor_testcase.git

Instala las dependencias necesarias:

    rosdep install --from-paths src --ignore-src -r -y

Compila el workspace:

    cd ~/easynav_ws
    colcon build
    source install/setup.bash

---

## 🧩 Requisitos

Este paquete está diseñado para usarse junto a:

- [**EasyNavigation**](https://github.com/jizqug00/EasyNavigation.git): framework de navegación modular.  
- [**easynav_plugins**](https://github.com/jizqug00/easynav_plugins.git): plugins para EasyNavigation (locallizers, maps managers, planners, controllers). 
- [**easynav_playground_kobuki**](https://github.com/EasyNavigation/easynav_playground_kobuki.git): entorno de simulación indoor con el robot Kobuki.

ROS 2 compatible: **Humble** (también probado en Rolling).

---

### Entornos incluidos

| Mapa         | Descripción                         |
|---------------|-------------------------------------|
| `home`        | Entorno doméstico simple            |
| `home2`       | Variante del entorno home           |
| `warehouse`   | Entorno tipo almacén (warehouse)    |
| `default`     | Mapa genérico de ejemplo            |

Puedes cambiar qué mapa usar editando el archivo YAML o pasando argumentos al launch según tu configuración.

---

## 📁 Parámetros

Los archivos en `robots_params/` permiten configurar:

- **Costmaps** (occupancy grids, inflation layers, etc.)
- **Mapeo** (modo SLAM / exploración)
- **Configuraciones multirrobot**
- **Escenarios personalizados (serest, dummy)**

Estos parámetros son usados por los nodos de EasyNavigation para configurar comportamiento y planificación en tiempo de ejecución.

---

## 🙏 Acknowledgements

Developed at the **Intelligent Robotics Lab (Universidad Rey Juan Carlos)**.  
Part of the Easy Navigation (EasyNav) project.