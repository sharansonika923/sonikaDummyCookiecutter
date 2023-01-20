import os
os.system("ng new {{cookiecutter.projectname}}")
os.chdir("{{cookiecutter.projectname}}")
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
