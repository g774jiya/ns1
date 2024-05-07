#include <iostream>
#include <string>
using namespace std;

string vigenere_encrypt(string plain_text, string key) {
    string cipher_text = "";
    int key_index = 0;
    for (char& c : plain_text) {
        if (isalpha(c)) {
            int shift = tolower(key[key_index % key.length()]) - 'a';
            cipher_text += (tolower(c) - 'a' + shift) % 26 + 'a';
            key_index++;
        } else {
            cipher_text += c;
        }
    }
    return cipher_text;
}

string vigenere_decrypt(string cipher_text, string key) {
    string plain_text = "";
    int key_index = 0;
    for (char& c : cipher_text) {
        if (isalpha(c)) {
            int shift = tolower(key[key_index % key.length()]) - 'a';
            plain_text += (tolower(c) - 'a' - shift + 26) % 26 + 'a';
            key_index++;
        } else {
            plain_text += c;
        }
    }
    return plain_text;
}

int main() {
    string text = "Hello, world!";
    string key = "key";
    string encrypted_text = vigenere_encrypt(text, key);
    cout<<text;
    cout << "\nEncrypted: " << encrypted_text << endl;
    string decrypted_text = vigenere_decrypt(encrypted_text, key);
    cout << "\nDecrypted: " << decrypted_text << endl;
    return 0;
}
