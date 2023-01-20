import os
os.system("ng new {{cookiecutter.angularprojectname}}")
os.chdir("{{cookiecutter.angularprojectname}}")
os.system("ng generate component login")
os.system("ng generate component signup")
routes = """
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';

const routes: Routes = [
{ path: 'login', component: LoginComponent },
{ path: 'signup', component: SignupComponent }
];

@NgModule({
imports: [RouterModule.forRoot(routes)],
exports: [RouterModule]
})
export class AppRoutingModule { }
"""

with open("src/app/app-routing.module.ts", "w") as f:
f.write(routes)

login="""
<form>
  <div class="imgcontainer">
    <img src="img_avatar2.png" alt="Avatar" class="avatar">
  </div>

  <div class="container">
    <label for="uname"><b>Username</b></label>
    <input type="text" placeholder="Enter Username" name="uname" required>

    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="psw" required>

    <button type="submit">Login</button>
    <label>
      <input type="checkbox" checked="checked" name="remember"> Remember me
    </label>
  </div>

  <div class="container" style="background-color:#f1f1f1">
    <button type="button" class="cancelbtn">Cancel</button>
    <span class="psw">Forgot <a href="#">password?</a></span>
  </div>
</form>
"""
with open("src/app/login/login.component.html", "w") as f:
f.write(login)

