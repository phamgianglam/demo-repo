import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable, of } from 'rxjs';
import { User } from '../type'

@Injectable({
  providedIn: 'root'
})
export class UserService {
  BASE_URL = 'http://127.0.0.1:8000/api/user'
  constructor(private http: HttpClient) {

  }
  async getUsers() {
    return this.http.get<User[]>(this.BASE_URL).toPromise()

  }

  async deleteUser(id: string) {
    let URL = `${this.BASE_URL}/${id}`
    console.log(URL)
    return this.http.delete<User>(URL).toPromise()
  }

  async getUser(id: string) {
    let URL = `${this.BASE_URL}/${id}`
    return this.http.get<User>(URL).toPromise()
  }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.log(error)

      return of(result as T);
    }
  }
}
