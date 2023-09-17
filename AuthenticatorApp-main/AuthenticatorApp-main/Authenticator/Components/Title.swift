//
//  Title.swift
//  Authenticator
//
//  Created by Emil Holmgaard on 11/02/2023.
//

import SwiftUI

struct Title: View {
    var body: some View {
        Text("Authenticator")
            .bold()
            .font(.title)
            .foregroundColor(.white)
    }
}

struct Title_Previews: PreviewProvider {
    static var previews: some View {
        Title()
            .background(Color.black)
    }
}
