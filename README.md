# MLOps-Personal
Basic projects to learn about MLOps

flowchart TD
    A[INICIO] --> B[1) INICIALIZACIÓN<br/>a) Fijar parámetros (α, β, ρ, m, Tmax)<br/>b) Asignar τ₀ a todos los (i, j)<br/>c) Lbest = ∞]

    B --> C[2) BUCLE PRINCIPAL]

    subgraph LP["Mientras T < Tmax"]
        C --> D[a) CONSTRUCCIÓN DE SOLUCIONES]

        subgraph CONS["Para cada hormiga k = 1..m"]
            D1[Construir ruta completa i → j]
            D2[Regla de probabilidad P(i,j)<br/>(pondera feromona τ y heurística η)]
            D3[Calcular longitud total Lk]
            D1 --> D2 --> D3
        end

        D --> E[b) ACTUALIZACIÓN DE LA MEJOR SOLUCIÓN<br/>Si alguna Lk mejora, Lbest ← Lk]

        E --> F[c) ACTUALIZACIÓN DE FEROMONAS]
        F --> F1[i) Evaporación: τ ← (1 − ρ) · τ en todos los (i, j)]
        F --> F2[ii) Depósito: en aristas usadas por k<br/>Δτ(i,j) += Σ (1 / Lk)]

        F1 --> G[d) Incrementar contador: T ← T + 1]
        F2 --> G

        G --> H{¿T < Tmax?}
        H -- Sí --> D
    end

    H -- No --> I[3) FIN<br/>Retornar Lbest y la ruta óptima asociada]
