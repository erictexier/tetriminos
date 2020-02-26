// utils anim
EasingFunctions = {
    // no easing, no acceleration
    linear: t => t,
    // accelerating from zero velocity
    easeInQuad: t => t*t,
    // decelerating to zero velocity
    easeOutQuad: t => t*(2-t),
    // acceleration until halfway, then deceleration
    easeInOutQuad: t => t<.5 ? 2*t*t : -1+(4-2*t)*t,
    // accelerating from zero velocity 
    easeInCubic: t => t*t*t,
    // decelerating to zero velocity 
    easeOutCubic: t => (--t)*t*t+1,
    // acceleration until halfway, then deceleration 
    easeInOutCubic: t => t<.5 ? 4*t*t*t : (t-1)*(2*t-2)*(2*t-2)+1,
    // accelerating from zero velocity 
    easeInQuart: t => t*t*t*t,
    // decelerating to zero velocity 
    easeOutQuart: t => 1-(--t)*t*t*t,
    // acceleration until halfway, then deceleration
    easeInOutQuart: t => t<.5 ? 8*t*t*t*t : 1-8*(--t)*t*t*t,
    // accelerating from zero velocity
    easeInQuint: t => t*t*t*t*t,
    // decelerating to zero velocity
    easeOutQuint: t => 1+(--t)*t*t*t*t,
    // acceleration until halfway, then deceleration 
    easeInOutQuint: t => t<.5 ? 16*t*t*t*t*t : 1+16*(--t)*t*t*t*t
}
// Code for 2d drawing 
function example_drawing(width, height, drawing_data)
{
    let canvas = document.getElementById("myCanvas");
    if (!canvas || !canvas.getContext)return;
    let ctx = canvas.getContext("2d");
    if (!ctx)return;
    let theduration = 30;
    let thetime = 0;
    let idinter = setInterval(draw_anim, theduration);
    let refresh = document.getElementById("refresh");

    function draw_anim()
    {
        ctx.clearRect(0, 0, width, height);
        thetime = thetime + 1./theduration;
        if (thetime > 1){
            clearInterval(idinter);
            thetime = 1;
        }
        for(i=0; i< drawing_data.length; i++) {
            let dt = drawing_data[i];
            let xbeg = dt[0][0];
            let ybeg = dt[0][1];
            let xend = dt[1][0];
            let yend = dt[1][1];
            let col = dt[2];
            let vary = EasingFunctions.easeInOutQuad(thetime) * EasingFunctions.easeInOutQuad(1-thetime);
            let radius = 12 + (15 * vary);
            let x = xbeg + ((xend - xbeg) * EasingFunctions.easeInOutQuad(thetime));
            let y = ybeg + ((yend - ybeg) * EasingFunctions.easeInOutQuad(thetime));
            ctx.beginPath();
            ctx.arc(x, y, radius, Math.PI*2, 0, false);
            ctx.fillStyle = col;
            ctx.fill();
            ctx.closePath();
        }
    }
    refresh.onclick = function restart_anim()
    {
        thetime = 0;
        idinter = setInterval(draw_anim, theduration);
    }
}
// Code for 3d drawing 
function Point3D(x,y,z) {
    this.x = x;
    this.y = y;
    this.z = z;

    this.rotateX = function(angle) {
        let rad, cosa, sina, y, z
        rad = angle * Math.PI / 180
        cosa = Math.cos(rad)
        sina = Math.sin(rad)
        y = this.y * cosa - this.z * sina
        z = this.y * sina + this.z * cosa
        return new Point3D(this.x, y, z)
    }

    this.rotateY = function(angle) {
        let rad, cosa, sina, x, z
        rad = angle * Math.PI / 180
        cosa = Math.cos(rad)
        sina = Math.sin(rad)
        z = this.z * cosa - this.x * sina
        x = this.z * sina + this.x * cosa
        return new Point3D(x,this.y, z)
    }

    this.rotateZ = function(angle) {
        let rad, cosa, sina, x, y
        rad = angle * Math.PI / 180
        cosa = Math.cos(rad)
        sina = Math.sin(rad)
        x = this.x * cosa - this.y * sina
        y = this.x * sina + this.y * cosa
        return new Point3D(x, y, this.z)
    }

    this.project = function(viewWidth, viewHeight, fov, viewDistance) {
        let factor, x, y
        factor = fov / (viewDistance + this.z)
        x = this.x * factor + (viewWidth / 2)
        y = this.y * factor + (viewHeight / 2)
        return new Point3D(x, y, viewDistance + this.z)
    }
}

// Define the colors for each face.
var colors = [[255,0,0],[0,255,0],[0,0,255],[255,255,0],[0,255,255],[255,0,255]];



/* Constructs a CSS RGB value from an array of 3 elements. */
function arrayToRGB(arr, al_pha) {
    if( arr.length == 3 ) {
        return "rgb(" + arr[0] + "," + arr[1] + "," + arr[2] + "," + al_pha + ")";
    }
    return "rgb(0,0,0,1)";
}

function example_drawing3d(width, height, drawing_data) {
    let canvas = document.getElementById("myCanvas");
    if (!canvas || !canvas.getContext)return;
    let ctx = canvas.getContext("2d");
    if (!ctx)return;
    ctx.lineWidth = .3;
    let theduration = 60;
    let thetime = 0;
    let idinter = setInterval(draw_anim3d, theduration);
    let refresh = document.getElementById("refresh");
    let angle = 0;
    let rantable = new Array();
    for(i=0; i< drawing_data.length; i++) {
        rantable.push(Math.random());
    }
    function draw_anim3d()
    {
        ctx.fillStyle = "rgb(255,255,255)";
        ctx.fillRect(0, 0, width, height);
    
        thetime = thetime + 1./theduration;
        if (thetime > 1){
            clearInterval(idinter);
            thetime = 1;
        }
        cube_size = .9;
        var localtime = EasingFunctions.easeInOutQuad(thetime)
        let vary = EasingFunctions.easeInOutQuad(thetime) * EasingFunctions.easeInOutQuad(1-thetime);
        angle = 360 * localtime;
        let al_pha = .7;
        for(i=0; i< drawing_data.length; i++) {
            let dt = drawing_data[i];
            let xbeg = dt[0][0];
            let ybeg = dt[0][1];
            let xend = dt[1][0];
            let yend = dt[1][1];
            let rgb = dt[2];
            let x = xbeg + ((xend - xbeg) * localtime);
            let y = ybeg + ((yend - ybeg) * localtime);
            let z = 20 * vary * rantable[i];
            if (i % 2){
                angle = -angle - (180 * vary * rantable[i]);
            }
            else {
                angle = angle + (180 * vary * rantable[i]);
            }
            draw_3d_cube(ctx, width, height, x, y, z, cube_size, rgb, al_pha, angle)
        }
    }

    refresh.onclick = function restart_anim3d() {
        thetime = 0;
        idinter = setInterval(draw_anim3d, theduration);
    }
}

// Define the vertices that compose each of the 6 faces. These numbers are
// indices to the vertex list defined above.
var faces  = [[0,1,2,3],[1,5,6,2],[5,4,7,6],[4,0,3,7],[0,4,5,1],[3,2,6,7]];

function draw_3d_cube(ctx, width, height, x, y, z, cube_size, rgb, al_pha, angle)
{
    const focal = 100.;
    const viewdistance = 1;
    let t = new Array();
    let vertices = [
        new Point3D(-cube_size, cube_size, -cube_size),
        new Point3D(cube_size,  cube_size, -cube_size),
        new Point3D(cube_size,  -cube_size,-cube_size),
        new Point3D(-cube_size, -cube_size,-cube_size),
        new Point3D(-cube_size, cube_size, cube_size),
        new Point3D(cube_size,  cube_size, cube_size),
        new Point3D(cube_size,  -cube_size, cube_size),
        new Point3D(-cube_size, -cube_size, cube_size)
    ];
    for( let i = 0; i < vertices.length; i++ ) {
        let v = vertices[i];
        let r = v.rotateY(angle).rotateZ(angle).rotateX(angle);
        let p = r.project(width, height, focal, 10-z);

        // we do the translation after projection.....
        p.x = p.x + x - width/2;
        p.y = p.y + y - height/2;
        p.z = p.z + z;
        t.push(p)
    }

    let avg_z = new Array();

    for( let i = 0; i < faces.length; i++ ) {
        let f = faces[i];
        avg_z[i] = {"index":i, "z":(t[f[0]].z + t[f[1]].z + t[f[2]].z + t[f[3]].z) / 4.0};
    }

    avg_z.sort(function(a,b) {
        return b.z - a.z;
    });

    for( let i = 0; i < faces.length; i++ ) {
        let f = faces[avg_z[i].index]

        ctx.fillStyle = arrayToRGB(rgb, al_pha);
        ctx.beginPath()
        ctx.moveTo(t[f[0]].x,t[f[0]].y)
        ctx.lineTo(t[f[1]].x,t[f[1]].y)
        ctx.lineTo(t[f[2]].x,t[f[2]].y)
        ctx.lineTo(t[f[3]].x,t[f[3]].y)
        ctx.closePath()
        ctx.stroke()
        ctx.fill()
    }
}
