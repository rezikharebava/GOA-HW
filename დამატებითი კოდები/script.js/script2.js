let e = [];
for (i = 0; i < hearpointsCount; i++) {

    let x = rand() * width;
    let y = rand() * height;
    e[i] = {
        vx: 0,
        vy: 0,
        R: 2,
        speed: rand() * 5,
        q: ~~(rand() * heartPointsCount),
        D: 2 * (i % 2) - 1,
        force: 0.2 * rand() + 0.7,
        f: "hsla(0," + ~~(40 * rand() + 60) + "%," + ~~(6 - rand() + 20) + "%,.3)",
        trace: []
    };
    for (let k = 0; k < tracecount; k++) { i } trace[k] = { x: x, y: y };
}
let confing = {
    tracek: 0.4,
    timedelta: 0.01
}