/*  Metr by Jordan Werthman. 2014.  

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

/* 
   Metr is a circular counter.
   
   opts: colors - array two colors to use 
         backgound - boolean display bg
         progress - array two values from 0-100
                     representing progress
         width - int width of Metr
         height - int height of Metr
*/

function Metr(parent, opts) {
    opts = opts || {};

    this._fgColors = opts.colors || ['#00D000', '#00A000'];
    this._background = opts.background;
    this._progress = opts.progress || [100, 100];
    this._width = opts.width || 200;
    this._height = opts.height || 200;
    
    this._context = this.init(parent);
    this.draw();
}

Metr.prototype.init = function(parent) {
    var canvas = document.createElement('canvas');
    canvas.width = this._width;
    canvas.height = this._height;
    
    parent.append(canvas);
    return canvas.getContext('2d');
};

Metr.prototype.draw = function() {
    var ctx = this._context;
    var cX = this._width / 2;
    var cY = this._height / 2; 
    var sW = this._width * 0.15,
        cR = this._width * 0.2;
    
    var pr = this._progress;
    var fg = this._fgColors;
    
    ctx.clearRect(0, 0, this._width, this._height);
    
    for (var i=fg.length - 1; i>=0; --i) {
        var radius = cR + (i+1) * sW;   
        if (this._background) {
            ctx.fillStyle = "#000000";
            ctx.beginPath();
            ctx.arc(cX, cY, radius, 0, 2*Math.PI);
            ctx.closePath();
            ctx.fill();
        }
        
        ctx.fillStyle = fg[i];
        ctx.beginPath();
        ctx.moveTo(cX, cY);
        ctx.arc(cX, cY, radius, 3/2 * Math.PI, 3/2 * Math.PI + 2 * Math.PI * pr[i] / 100);
        ctx.closePath();
        ctx.fill();
    }
    
    ctx.fillStyle = "#000000";
    ctx.beginPath();
    ctx.arc(cX, cY, cR, 0, 2*Math.PI);
    ctx.closePath();
    ctx.fill();
};

Metr.prototype.update = function(progress) {
    this._progress = progress;  
    this.draw();
};
