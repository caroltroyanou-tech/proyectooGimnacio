<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>FITTNES.GIRLS</title>
    <style>
x        body { font-family: Arial, sans-serif; margin: 30px; background-color: #f4f7f6; background-image: url("images_1.jpeg"); }
        h1, h2 { color: #333; }
        .container { display: flex; gap: 40px; }
        .box { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); width: 50%; }
        table { width: 100%; border-collapse: collapse; margin-top: 15px; }
        th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }
        th { background-color: #007bff; color: white; }
        form { display: flex; flex-direction: column; gap: 10px; }
        input, select, button { padding: 10px; font-size: 14px; border-radius: 4px; border: 1px solid #ccc; }
        button { background-color: #28a745; color: white; border: none; cursor: pointer; }
        button:hover { background-color: #218838; }
        .btn-edit { background-color: #ffc107; color: #212529; font-size: 12px; padding: 5px 10px; }
        .btn-edit:hover { background-color: #e0a800; }
        .cancel-mode { background-color: #6c757d; display: none; }
        
    </style>
</head>
<body>

    <h1>🏋️ Fittnes.Girls</h1>
    <h2>Gestion de socios y planes</h2>
    <hr>

    <div class="container">
        <!-- SECCIÓN TABLA (GET) -->
        <div class="box">
            <h2>👥 Listado de Socios Activos</h2>
            <table id="tabla-socios">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nombre Completo</th>
                        <th>Plan Inscrito</th>
                        <th>Entrenador</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- Dinámico -->
                </tbody>
            </table>
        </div>

        <!-- SECCIÓN FORMULARIO (POST / PUT) -->
        <div class="box">
            <h2 id="form-title">➕ Registrar Nuevo Socio</h2>
            <form id="form-socio">
                <!-- Input oculto para guardar el ID cuando se edita -->
                <input type="hidden" id="socio-id">

                <label>Nombre:</label>
                <input type="text" id="nombre" required placeholder="Ej. Juan">

                <label>Apellido:</label>
                <input type="text" id="apellido" required placeholder="Ej. Pérez">

                <label>Seleccionar Plan Membresía:</label>
                <select id="plan_asignado" required>
                    <option value="">Selecciona tu plan</option>
                    <option value="">Musculacion </option>
                    <option value="">Grupales </option>
                    <option value="">Crossfit </option>
                </select>

                <label>Asignar Entrenador Personal:</label>
                <select id="entrenador_personal">
                    <option value="">Selecciona tu entrenador </option>
                    <option value="">Andres Felipe Troches</option>
                    <option value="">Kevin Stiven Vasquez</option>
                    <option value="">Ana Milena Fajarso</option>
                </select>

                <button type="submit" id="btn-submit">Guardar Registro</button>
                <button type="button" id="btn-cancel" class="cancel-mode" onclick="cancelarEdicion()">Cancelar Edición</button>
            </form>
        </div>
    </div>

    <script>
        const BASE_API_URL = "http://127.0.0";
        let modoEdicion = false;

        // 1. CARGA DINÁMICA: Obtener listados para los Selects del formulario
        async function cargarSelects() {
            try {
                // Obtener Planes
                const resPlanes = await fetch(`${BASE_API_URL}planes/`);
                const planes = await resPlanes.json();
                const selectPlanes = document.getElementById("plan_asignado");
                selectPlanes.innerHTML = '<option value="">-- Seleccione un Plan --</option>';
                planes.forEach(p => {
                    selectPlanes.innerHTML += `<option value="${p.id}">${p.nombre_plan} ($${p.precio})</option>`;
                });

                // Obtener Entrenadores
                const resEntrenadores = await fetch(`${BASE_API_URL}entrenadores/`);
                const entrenadores = await resEntrenadores.json();
                const selectEntrenadores = document.getElementById("entrenador_personal");
                selectEntrenadores.innerHTML = '<option value="">Ninguno / Por asignar</option>';
                entrenadores.forEach(e => {
                    selectEntrenadores.innerHTML += `<option value="${e.id}">${e.nombre} - ${e.especialidad}</option>`;
                });
            } catch (error) {
                console.error("Error al poblar los elementos de selección:", error);
            }
        }

        // 2. GET: Cargar tabla de socios
        async function cargarSocios() {
            try {
                const response = await fetch(`${BASE_API_URL}socios/`);
                const socios = await response.json();
                const tbody = document.querySelector("#tabla-socios tbody");
                tbody.innerHTML = ""; 

                socios.forEach(socio => {
                    const row = `<tr>
                        <td>${socio.id}</td>
                        <td>${socio.nombre} ${socio.apellido}</td>
                        <td>${socio.nombre_plan || 'Sin Plan'}</td>
                        <td>${socio.nombre_entrenador || 'No asignado'}</td>
                        <td>
                            <button class="btn-edit" onclick="prepararEdicion(${socio.id}, '${socio.nombre}', '${socio.apellido}', ${socio.plan_asignado}, ${socio.entrenador_personal})">Editar</button>
                        </td>
                    </tr>`;
                    tbody.innerHTML += row;
                });
            } catch (error) {
                console.error("Error al obtener los socios:", error);
            }
        }

        // 3. PREPARAR INTERFAZ PARA EDITAR (PUT)
        function prepararEdicion(id, nombre, apellido, planId, entrenadorId) {
            modoEdicion = true;
            document.getElementById("form-title").innerText = `✏️ Editar Socio #${id}`;
            document.getElementById("btn-submit").innerText = "Actualizar Registro";
            document.getElementById("btn-submit").style.backgroundColor = "#ffc107";
            document.getElementById("btn-submit").style.color = "#000";
            document.getElementById("btn-cancel").style.display = "block";

            // Asignar los valores vigentes al formulario
            document.getElementById("socio-id").value = id;
            document.getElementById("nombre").value = nombre;
            document.getElementById("apellido").value = apellido;
            document.getElementById("plan_asignado").value = planId || "";
            document.getElementById("entrenador_personal").value = entrenadorId || "";
        }

        // 4. CANCELAR MODO EDICIÓN
        function cancelarEdicion() {
            modoEdicion = false;
            document.getElementById("form-socio").reset();
            document.getElementById("form-title").innerText = "➕ Registrar Nuevo Socio";
            document.getElementById("btn-submit").innerText = "Guardar Registro";
            document.getElementById("btn-submit").style.backgroundColor = "#28a745";
            document.getElementById("btn-submit").style.color = "white";
            document.getElementById("btn-cancel").style.display = "none";
        }

        // 5. PROCESAR PROCESO DE ENVÍO (POST o PUT)
        document.getElementById("form-socio").addEventListener("submit", async (e) => {
            e.preventDefault();

            const id = document.getElementById("socio-id").value;
            const entrenadorVal = document.getElementById("entrenador_personal").value;

            const datosSocio = {
                nombre: document.getElementById("nombre").value,
                apellido: document.getElementById("apellido").value,
                plan_asignado: parseInt(document.getElementById("plan_asignado").value),
                entrenador_personal: entrenadorVal ? parseInt(entrenadorVal) : null
            };

            let url = `${BASE_API_URL}socios/`;
            let método = "POST";

            if (modoEdicion) {
                url = `${BASE_API_URL}socios/${id}/`;
                método = "PUT";
            }

            try {
                const response = await fetch(url, {
                    method: método,
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(datosSocio)
                });

                if (response.ok) {
                    alert(modoEdicion ? "¡Socio actualizado con éxito!" : "¡Socio creado con éxito!");
                    cancelarEdicion();
                    cargarSocios();
                } else {
                    alert("Error en la operación. Revise los campos enviados.");
                }
            } catch (error) {
                console.error("Error en la petición HTTP:", error);
            }
        });

        // Orquestación Inicial al Abrir la Ventana
        window.onload = async function() {
            await cargarSelects();
            await cargarSocios();
        };
    </script>
</body>
</html>
