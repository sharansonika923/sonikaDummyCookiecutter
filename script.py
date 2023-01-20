import os

# Create the Angular project
os.system("ng new newproject")

# Navigate into the project directory
os.chdir("newproject")

# Create the login component
os.system("ng generate component login")

# Create the signup component
os.system("ng generate component signup")

# Add routes for the login and signup components
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
