import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Config } from './config';
@Injectable({
  providedIn: 'root'
})
export class AlumnoService {

  public url: String;
  private http: HttpClient;

  constructor( http: HttpClient) {
    this.http = http;
    this.url = Config.apiUrl;
   }
  //any data
  add(data: any){
    return this.http.post(this.url + 'anysinformation/', data);
  }

  update(data: any, id: number) {
    return this.http.put(this.url + 'anysinformation/' + id, data);
  }

  delete(id: number)  {
    return this.http.delete(this.url + 'anysinformation/' + id);
  }

  get( id: number ) {
    return this.http.get(this.url + 'anysinformation/' + id);
  }

  getAll() {
    return this.http.get(this.url + 'anysinformation/');
  }


}
